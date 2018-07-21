import functools


def autolog():
    def trace_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if type(func) is types.MethodType:
                funcName = func.func_globals['__name__'] + '.' + func.func_name
            else:
                funcName = func.func_name
            # funcName = func.func_name if func.func_name != '__init__' else func.func_globals['__name__'] + '.__init__'
            print 'Entered ' + funcName + ' called with ' + 'args=' + str(args) + ' and kwargs=' + str(kwargs)
            retVal = func(*args, **kwargs)
            print 'Exited {0}'.format(funcName)
            return retVal
        return inner
    return trace_decorator


class A:
    @autolog()
    def A_foo(self,):
        print 'In Foo'

@autolog()
def foo():
    pass

import types

Aobj = A()

Aobj.A_foo()

foo()