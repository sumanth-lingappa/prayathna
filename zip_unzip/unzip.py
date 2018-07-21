import shutil

archive_name = 'sumanth'
fmt = '7z'
root_dir = 'D:\workspace\personal\sample\zip_unzip\Files'

shutil.make_archive(archive_name, fmt, root_dir)

print shutil.get_archive_formats()