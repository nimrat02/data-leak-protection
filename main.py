import sys
import time
from datetime import datetime

import os
import csv

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def __init__(self):
        file_exists = os.path.isfile('Events.csv')
        self.wr = open("Events.csv", "a")
        self.event_writer = csv.writer(self.wr)

        fields = ['Date', 'Time', 'Type', 'Name', 'Path', 'Action']
        if not file_exists:
            self.event_writer.writerow(fields)

    def on_created(self, event):
        file_type = 'Directory' if event.is_directory else 'File'
        now = datetime.now()
        data = [now.date(), now.time(), file_type, os.path.basename(event.src_path),
                event.src_path, "Created"]
        self.event_writer.writerow(data)

    def on_deleted(self, event):
        file_type = 'Directory' if event.is_directory else 'File'
        now = datetime.now()
        data = [now.date(), now.time(), file_type, os.path.basename(event.src_path),
                event.src_path, "Deleted"]
        self.event_writer.writerow(data)

    def on_modified(self, event):
        file_type = 'Directory' if event.is_directory else 'File'
        now = datetime.now()
        data = [now.date(), now.time(), file_type, os.path.basename(event.src_path),
                event.src_path, "Modified"]
        self.event_writer.writerow(data)

    def __del__(self):
        self.wr.close()


if __name__ == '__main__':

    event_handler = Handler()

    if len(sys.argv) != 2:
        print("Invalid number of arguments. Enter 'python3 main.py <filepath>'")
        sys.exit()

    # taking file path as argument from user
    path = sys.argv[1]

    if not os.path.exists(os.path.abspath(path)):
        print('Enter valid file path.')
        sys.exit()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        print("Monitoring starts")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring ends")

    observer.join()
