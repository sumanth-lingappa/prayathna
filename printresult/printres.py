from inputdata import PROJECTDATA

print '-'*100
print "{:<15}{:<15}{:<50}{:<10}{:<10}".format('PROJECT','SUITE','TESTCASE','STATUS','ERRORS')
print '-'*100
pproj = ''
psuite = ''
projList = sorted(PROJECTDATA.keys())
for proj in projList:
    projData = PROJECTDATA[proj]
    suiteList = sorted(projData['suite'].keys())
    for suite in suiteList:
        suiteData = projData['suite'][suite]
        tcList = sorted(suiteData.keys())
        for tc in tcList:
            tcData = suiteData[tc]
            status = tcData['status']
            error = tcData['error']

            pproj = proj if pproj != proj else ''
            psuite = suite if psuite != suite else ''

            print "{:<15}{:<15}{:<50}{:<10}{:<10}".format(pproj,psuite,tc,status,error)
            pproj = proj
            psuite = suite

print '-'*100


