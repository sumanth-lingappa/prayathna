class A(object): x = 'A'
class B(object): x = 'B'
class C(A): pass
class D(B,C): pass

print D.mro()


class Parent():
    def __init__(self):
        self.__pvtvar = 'pvtvar'
        self.pubvar = 'pubvar'


class Child(Parent):

    def changePvtVar(self):
        self.__pvtvar = 'changed pvtvar'
        print self.__pvtvar


c = Child()
c.changePvtVar()

print c._Child__pvtvar
