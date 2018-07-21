import os

if os.name == 'nt':
    import winutils as utils
elif os.name == 'posix':
    import linuxutils as utils


utils.foo()