
def power(a, b):
    res = 1

    while b:
        if b & 1:
            res *= a
        b >>= 1
        a *= a
    return res


#print power(4,3)

