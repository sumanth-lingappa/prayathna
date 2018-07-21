import ConfigParser
import datetime
import os
import sys

HOMELIST = os.path.abspath(__file__) #.split(os.sep)
HOMEDIR = os.sep.join(HOMELIST[:-2])

print os.path.defpath

#print HOMELIST
#print HOMEDIR

PROJECTDATA = [{'project': 'SUMANTH', 'setup': 'DIFF_UPDATE_SUIE', 'suitelist': ['sumanthsuite.ini'], 'suitedata': [{'suite': 'sumanthsuite.ini', 'tclist': ['SUMANTHproject\\Test_case_pass.py'], 'tcdata': [{'status': 'FAIL', 'warn': 0, 'tcname': 'TestCasePassSumanth', 'excp': 1, 'error': 3}]}]}]

import pprint

pprint.pprint(PROJECTDATA)