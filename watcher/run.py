import os
import sys
from argparse import ArgumentParser

from watchdog.observers import Observer

from watcher import EventHandler


def main():
    parser = ArgumentParser()
    parser.add_argument('path', help='path to watch')
    args = parser.parse_args()
    if not os.path.exists(args.path):
        sys.exit('Directory {} does not exist'.format(args.path))

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=args.path, recursive=False)

    try:
        observer.start()
        observer.join()
    except (KeyboardInterrupt, Exception, ):
        observer.stop()
