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
    # print dirpath
    # print dirnames
    # print filenames
    # print ''

    print 'size:\tfp'
    for f in filenames:
        fp = os.path.join(dirpath, f)
        tmp_size = os.path.getsize(fp)
        print '{}:\t{}'.format(tmp_size, fp)
        total_size += tmp_size

print "total size of directory is {}".format(total_size)

