import os
def p_GetTestCase(fname):
    TCLIST = []
    with open(fname, 'r') as f:
        flines = [line.strip() for line in f.readlines()]
        for line in flines:
            if line and not line.startswith('#'):
                # line = line.replace('\n', '')
                # line = line.replace('\r\n','')
                line = line.replace('\\',os.sep)
                TCLIST.append(line)
    return TCLIST


print p_GetTestCase('SUMAsuite.ini')

