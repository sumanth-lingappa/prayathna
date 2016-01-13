__author__ = 'Sumanth_Lingappa'


def initializeTable(length):
    return [[False for i in range(length)] for j in range(length)]

def largestPalind(s):
    table = initializeTable(len(s))
    longPalindr = ''

    for i in range(len(s)):
        table[i][i] = True

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            longPalindr = table[i][i+1]

    for pLen in range(3,len(s)):
        for i in range(len(s) - pLen + 1):
            j = i + pLen - 1
            if s[i] == s[j] and table[i+1][j-1] == True:
                table[i][j] = True
                longPalindr = s[i:j+1]

    return longPalindr



print largestPalind('forgeeksskeegfor')
