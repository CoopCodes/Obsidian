import datetime
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ignore = [
    '.gitattributes',
]

class FileHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_modified(self, event):
        global git_ignore
        for filename in os.listdir(self.directory):
            if not(filename in ignore):
                file_path = os.path.join(self.directory, filename)
                subprocess.check_call(['git', 'add', '.'], cwd=self.directory)
                try:
                    subprocess.check_call(f'git commit -m "auto: {filename}"', cwd=self.directory)
                except subprocess.CalledProcessError:
                    pass
                try:
                    subprocess.check_call(['git', 'push'], cwd=self.directory)
                except subprocess.CalledProcessError:
                    continue

def git_init(directory):
    try:
        subprocess.check_call(['git', 'pull'], cwd=directory)
    except subprocess.CalledProcessError:
        subprocess.check_call(['git', 'add', '.'], cwd=directory)
        subprocess.check_call(['git', 'commit', '-m', str(datetime.datetime.now())], cwd=directory)
        subprocess.check_call(['git', 'push'], cwd=directory)
        
        subprocess.check_call(['git', 'pull'], cwd=directory)


def monitor_directory(directory):
    event_handler = FileHandler(directory)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory = 'C:\\Users\\gc021217\\Obsidian\\Obsidian'  # specify your directory
    git_init(directory)
    monitor_directory(directory)