import sys,logging
logging.basicConfig(
    level=logging.DEBUG, stream=sys.stdout,
    format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")

#@logged
class Sample:
    def test(self):
        self.__log.debug("This is a test.")

Sample().test()
