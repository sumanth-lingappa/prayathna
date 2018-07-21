def mapPattern(sString, sPattern, oPattern, fOutput=''):
    if len(sPattern) == 0 and len(sString) == 0:
        return fOutput

    if len(sPattern) > 1 and sPattern[0] == "*" and  len(sString) == 0:
        return False

    if (len(sPattern) != 0 and len(sString) !=0 and sPattern[0] == sString[0]):
        if len(oPattern) != 0:
            fOutput += (oPattern[0], '')[oPattern[0] == "*"]
            oPattern = oPattern[1:]
        return mapPattern(sString[1:], sPattern[1:], oPattern, fOutput)

    if len(sPattern) !=0 and sPattern[0] == "*":
        if oPattern[0] == "*":
            fOutput += sString[0]
            sString = sString[1:]
            sPattern = sPattern[1:]
        else:
            fOutput += oPattern[0]
        return mapPattern(sString, sPattern, oPattern[1:], fOutput)
    else:
        return mapPattern(sString[1:], sPattern, oPattern, fOutput + sString[0])


sString = "sconfig.dll_p" #ids.wnt
sPattern = "*.dll_p" # *.wnt
oPattern = "*.dll" # *.dat


#print mapPattern(sString,sPattern,oPattern)

sString = "ids.wnt"
sPattern = "*.wnt"
oPattern = "*.dat"

print mapPattern(sString,sPattern,oPattern)
