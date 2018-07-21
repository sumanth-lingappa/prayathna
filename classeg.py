
class Employee1(object):
    pass

ea1 = Employee1()

class Employee(object):
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(selfself):
        print 'Total Employee %d' % Employee.empCount

    def displayEmployee(self):
        print "name is {} and salary is {}".format(self.name.upper(),self.salary)

    def __del__(self):
        # Employee.empCount -= 1
        print " {} destroyed".format(self.__class__.__name__)

e1 = Employee('sumanth',2000000)
e2 = Employee('rachitha', 99999999)

e1.displayCount()

e2.displayCount()

# print Employee.name

e1.displayEmployee()
e2.displayEmployee()

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

repr(e1)
print cmp(e1,e1)
print type(e1)
print type(e2)
if type(e1) == type(e2):
    print 'both objects point to same base'
