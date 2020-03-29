import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


docs_ext = ('doc', 'docx', 'xls', 'xlsx', 'html', 'pdf', 'odf',
            'txt', 'ppt', 'pptx', )
media_ext = ('jpg', 'jpeg', 'png', 'gif', 'heic', 'mp4', 'avi', )
# TODO: get path from cmd args
BASE_PATH = '/Users/biryukovsky/Downloads/'


def get_folder(ext: str):
    ext = ext.replace('.', '').lower()
    if ext in docs_ext:
        return 'Docs'
    elif ext in media_ext:
        return 'Media'
    else:
        return 'Other'


class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return False

        t = int(time.time())

        path, ext = os.path.splitext(event.src_path)
        filename = os.path.basename(path)
        filename = '{}-{}{}'.format(filename, t, ext)

        folder = get_folder(ext)
        path_to_move = os.path.join(BASE_PATH, folder)

        shutil.move(event.src_path, os.path.join(path_to_move, filename))

        return True
