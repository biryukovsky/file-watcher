import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


docs_ext = ('doc', 'docx', 'xls', 'xlsx', 'html', 'pdf', 'odf',
            'txt', 'ppt', 'pptx', )
media_ext = ('jpg', 'jpeg', 'png', 'gif', 'heic', 'mp4', 'avi', )


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

        base, file = os.path.split(event.src_path)
        filename, ext = os.path.splitext(file)
        filename = '{}-{}{}'.format(filename, t, ext)

        folder = get_folder(ext)
        path_to_move = os.path.join(base, folder)

        shutil.move(event.src_path, os.path.join(path_to_move, filename))

        return True
