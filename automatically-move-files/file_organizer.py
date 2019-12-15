# idea courtesy: https://www.youtube.com/watch?v=qbW6FRbaSl0

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import pathlib

username = ''  # username

folder_to_track = '/mnt/c/Users/{}/Downloads/'.format(username)
image_destination = '/mnt/c/Users/{}/Pictures/'.format(username)
doc_destination = '/mnt/c/Users/{}/Documents/'.format(username)
music_destination = '/mnt/c/Users/{}/Music/'.format(username)
video_destination = '/mnt/c/Users/{}/Videos/'.format(username)


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            print('Processing file: {}'.format(filename))
            filetype = pathlib.Path(filename).suffix.lower()
            if filetype in ['.rar', '.zip', '.7z', '.tar', '.gz', '.msi', '.exe', '.html', '.ppt', '.pptx', '.doc', '.docx', '.pdf', '.rtf', '.csv', '.lic', '.xls', '.xlsx', '.json']:
                folder_destination = doc_destination
                if filename.startswith('ChatLog') and filetype in ['.rtf']:
                    folder_destination += os.sep + 'GTMchats'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.ppt', '.pptx']:
                    folder_destination += os.sep + 'Presentations'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.csv', '.xls', '.xlsx']:
                    folder_destination += os.sep + 'Excels'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.pdf']:
                    folder_destination += os.sep + 'PDFs'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.lic']:
                    folder_destination += os.sep + 'Licences'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.html', '.htm']:
                    folder_destination += os.sep + 'Webpages'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.msi', '.exe']:
                    folder_destination += os.sep + 'Software'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
                elif filetype in ['.rar', '.zip', '.7z', '.tar', '.gz']:
                    folder_destination += os.sep + 'Compressed'
                    if not os.path.exists(folder_destination):
                        os.makedirs(folder_destination)
            elif filetype in ['.png', '.gif', '.jpeg', '.jpg']:
                folder_destination = image_destination
            elif filetype in ['.wlmp', '.mp4', '.avi']:
                folder_destination = video_destination
            elif filetype in ['.mp3']:
                folder_destination = music_destination
            else:
                print('Unknown filetype: {} : Not processing'.format(filetype))
                continue
            src = folder_to_track + os.sep + filename
            new_destination = folder_destination + os.sep + filename
            os.rename(src, new_destination)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
