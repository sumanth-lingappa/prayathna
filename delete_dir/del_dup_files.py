import os

path = '.'
total_size = 0

def hashfile(path, blocksize = 65536):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read()
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read

for dirpath, dirnames, filenames in os.walk(path):
    print dirpath
    print dirnames
    print filenames
    print ''

    for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)

print "total size of directory is {}".format(total_size)

