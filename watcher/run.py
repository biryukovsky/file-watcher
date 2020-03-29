from watchdog.observers import Observer

from watcher import EventHandler, BASE_PATH


def main():
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=BASE_PATH, recursive=False)

    try:
        observer.start()
        observer.join()
    except (KeyboardInterrupt, Exception, ):
        observer.stop()
