import os,sys
HOMELIST = os.path.abspath(__file__).split(os.sep)
HOMEDIR = os.sep.join(HOMELIST[:-2])

while HOMEDIR in sys.path:
    sys.path.remove(HOMEDIR)
sys.path.append(HOMEDIR)


