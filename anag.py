__author__ = 'Sumanth_Lingappa'

#anagram strings

def isAnagr(s1,s2):
    if len(s1) != len(s2): return False

    sDict = {}
    for c in list(s1):
        temp = 0
        if c not in sDict.keys():
            sDict[c] = 1
        else:
            sDict[c] += 1


    for c in list(s2):
        if c not in sDict.keys(): return False
        if sDict[c] != s2.count(c): return False
    return True



print isAnagr('done','noode')