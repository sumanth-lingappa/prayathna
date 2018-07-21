import logging
from functools import wraps

LOG_FILENAME = "logging_example.out"
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    filemode="w",
                    )

def tracelog(log=logging):
    def trace_decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            log.debug("entered " + func.func_name + " called with " + "args=" + str(args) + " and kwargs=" + str(kwargs))
            func(*args, **kwargs)
            log.debug("exited {0}".format(func.func_name))
        return inner
    return trace_decorator

