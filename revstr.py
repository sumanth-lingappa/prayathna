__author__ = 'Sumanth_Lingappa'


def revStr(s):
    revS = ''
    for i in range(1, len(s)+1):
        revS += s[-i]
    return revS


#print revStr(' sumanth ')
