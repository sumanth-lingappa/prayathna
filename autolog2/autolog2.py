from __init__ import *

@tracelog()
def somefunc(s):
    pass

@tracelog()
def foo():
    somefunc("abc")


foo()
