patDict = {r"win.*.abc": "win.*.dll",
           r".*.xyz": ".*.exe",
           r".*.xyz_p": ".*.xyz",
          }

inData = ["windows.abc","linux.xyz","win_abc.abc","pqr.xyz_p"]
outData = []

import re

def patMap(outPat, data):
    ext = outPat.split(".")[-1]
    fname = data.split(".")[0]
    return ".".join([fname,ext])

for string in inData:
    for pat in patDict.keys():
        m = re.search(pat, string)
        if m:
            od = patMap(patDict[pat], string)
            outData.append(od)
            break

print outData
