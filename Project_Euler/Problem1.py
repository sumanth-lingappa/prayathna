'''
Problem Statement : If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
                    The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

URL : https://projecteuler.net/problem=1
'''

def sum_multiples_3_5(num):
    total = 0
    for n in range(num):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total



print sum_multiples_3_5(1000)