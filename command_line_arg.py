import sys

# print sys.argv

print 'the file name is {}'.format(sys.argv[0])

def f(*arg):
    for i in range(len(arg)):
        print arg[i]

p=(1,2,3,4,5)

f(*p)