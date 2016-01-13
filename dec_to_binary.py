__author__ = 'Sumanth_Lingappa'

# Python program to convert decimal number into binary number using recursive function

import sys
def binary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n < 1: return
   if n > 1:
       binary(n//2)
   sys.stdout.write(str(n%2))

# Take decimal number from user
dec = int(input("Enter an integer: "))
binary(dec)
