

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibiter(n):
    fiblist = [1,1]
    for i in range(3,n):
        fiblist.append(fiblist[-1]+fiblist[-2])
    return fiblist

def verifyfib(fiblist):
    for i in range(3, len(fiblist)):
        if fiblist[i] != fiblist[i-1] + fiblist[i-2]:
            return "Not fib sequence"
    return "fib sequence"

flist = fibiter(100)
print flist
print verifyfib(flist)
