__author__ = 'Sumanth_Lingappa'


def isPalindrome(s):
    #sRev = s[::-1]
    sRev = ''.join(reversed(s))
    print s,sRev
    if s == sRev:
        return True
    return False



print isPalindrome('suus')
