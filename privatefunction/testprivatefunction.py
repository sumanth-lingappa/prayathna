
class TestPvtFunction():
    name = 'sumanth'
    salary = '2000000000'
    def __init__(self):
        print '__init__() called'
        self.age = 30

    def __privatefunc(self):
        print '__privatefunc called'

    def publicfunc(self):
        print 'publicfunc called'


obj1 = TestPvtFunction()
obj1.publicfunc()
# obj1.__privatefunc()

print obj1.name

print vars(obj1)
print dir(obj1)
