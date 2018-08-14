"""
print the below using input as number of lines
Eg. If input is 5, then print

  *
 ***
*****
 ***
  *

"""


import sys

if len(sys.argv) != 2:
    usage = """Usage: star_triangle <num_of_lines>"""
    print usage
    sys.exit(0)

n = int(sys.argv[1])

for i in range(n):
    print ' '*(n-i) + '*'*(2*i) + ' '*(n-i)

print '*'*n

for i in range(n):
    print ' '*i + '*'*(n-i)

