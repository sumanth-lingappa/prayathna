from __init__ import *
def run_tests():
    from proboscis import TestProgram
    from testprob import testcase1

    # Run Proboscis and exit.
    TestProgram().run_and_exit()

if __name__ == "__main__":
    run_tests()