'''
Problem Statement : The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

URL : https://projecteuler.net/problem=2
'''

from itertools import islice, count
def isprime(num):
    isPrime = True
    for i in xrange(2,num):
        if num % i == 0:
            isPrime = False
            break
    return isPrime

def primeList(fList):
    pList = []
    for i in fList:
        if isprime(i):
            pList.append(i)
    return pList

def factorList(num):
    fList = []
    for i in islice(count(),2, num):
        if num % i == 0:
            fList.append(i)
    return fList

# fList = factorList(600851475143)
fList = factorList(13195)
print sorted(primeList(fList),reverse=True)[0]

