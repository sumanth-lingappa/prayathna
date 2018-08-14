import weakref

class Factory(object):
    def __init__(self, cls, max_objects):
        self.product_class = cls
        self.max_objects = max_objects
        self.products = []

    def __call__(self, *args, **kwargs):
        self.products = [x for x in self.products if x() is not None] # filter out dead objects
        if len(self.products) < self.max_objects:
            new_product = self.product_class(*args, **kwargs)
            self.products.append(weakref.ref(new_product))
            return new_product
        else:
            return None


class MyClass:
    def __init__(self, *args, **kwargs):
        print args, kwargs

#This factory will create up to 2 instances of MyClass
#and refuse to create more until at least one of those
#instances have died.
factory=Factory(MyClass,2)
i1=factory("foo","bar"); print i1      #instance of MyClass
i2=factory("bar","baz"); print i2      #instance of MyClass
i3=factory("baz","chicken"); print i3  #None
