"""
add, edit, delete employee records.
Employee : Name, Emp.ID, age, designation, salary
"""


class Employee(object):
    def __init__(self, name, id, age, desgn, sal):
        self.name = name
        self.id = id
        self.age = age
        self.designation = desgn
        self.salary = sal

