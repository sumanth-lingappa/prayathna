import pefile
import os
import win32api

def p_GetFileVersionOLD(fname):  # Reviewed

        info = win32api.GetFileVersionInfo(fname,
                                           os.sep)  # GetFileVersionInfo(Filename, SubBlock) SubBloc= \\ for VS_FIXEDFILEINFO
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return [str(win32api.HIWORD(ms)), str(win32api.LOWORD(ms)), str(win32api.HIWORD(ls)),
                str(win32api.LOWORD(ls))]


def p_GetFileVersionNEW(fname):  # Reviewed
    def LOWORD(dword):
        return dword & 0x0000ffff

    def HIWORD(dword):
        return dword >> 16

    pe = pefile.PE(fname)
    # FileVersion = pe.FileInfo[0].StringTable[0].entries['FileVersion']
    # print FileVersion


    ms = pe.VS_FIXEDFILEINFO.FileVersionMS
    ls = pe.VS_FIXEDFILEINFO.FileVersionLS
    return [str(HIWORD(ms)), str(LOWORD(ms)), str(HIWORD(ls)),
            str(LOWORD(ls))]


path = 'C:\Program Files\Quick Heal\Quick Heal Total Security\SAFEBANK.EXE'
print p_GetFileVersionOLD(path)
import time
now1 = time.time()
print p_GetFileVersionNEW(path)
now2 = time.time()
print now2-now1
