import logging
import sys

import nose

logging.basicConfig(level=logging.DEBUG)

#here are some tests in this module
def test_me():
    pass

if __name__ == "__main__":
    #This code will run the test in this file.'

    module_name = sys.modules[__name__].__file__
    logging.debug("running nose for package: %s", module_name)

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            "-v"])
    logging.info("all tests ok: %s", result)