

def getEvens(l):
    return [e for e in l if e%2 == 0]

l = range(10)
print getEvens(l)



fo = open("foo.txt", "w")

print fo.fileno()