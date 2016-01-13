__author__ = 'Sumanth_Lingappa'

def msb(num):
    bitpos = 0
    while num:
        num >>= 1
        bitpos += 1
    return bitpos - 1 # Including zero as bit-position


print msb(2567)
