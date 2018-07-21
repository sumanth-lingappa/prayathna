import os
import win32com.client as com

def directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def p_GetDirSize(dirpath):
    """
Author: Amol Vyavahare.
Date: 25-May-15
Purpose: Get size of the directory in MB.
Arguments: path : Complete path of the directory.
Example : p_GetDirSize(r"C:\logs")
Return value : Returns size of the directory tree.
"""

    fso = com.Dispatch("Scripting.FileSystemObject")
    folder = fso.GetFolder(dirpath)
    MB = 1
    # MB=1024*1024.0
    lv_size = (folder.Size / MB)

    return lv_size



dirpath = 'D:\workspace\New_FW\QHAuto'
print directory_size(dirpath)
print p_GetDirSize(dirpath)
