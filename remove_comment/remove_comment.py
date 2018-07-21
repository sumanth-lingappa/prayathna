import re

fo = open('file.txt','r')

flines = fo.readlines()
fo.close()

fw = open('file.txt','w')

for line in flines:
    rline = re.sub(r'[ ]*#.*$','',line)
    fw.write(rline)

fw.close()


