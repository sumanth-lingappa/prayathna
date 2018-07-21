import os


class Linux:
    def __init__(self):
        print 'In Linux Constructor'

    def getpath(self):
        print 'In Linux->getpath()'
        return '/root/path'


class Windows:
    def __init__(self):
        print 'In Windows Constructor'

    def getpath(self):
        print 'In Windows->getpath()'
        return 'c:\path'

    def p_GetFileVersion(self,fname): #Reviewed
        from win32api import GetFileVersionInfo, LOWORD, HIWORD
        try:
            info = GetFileVersionInfo(fname, "\\")  # GetFileVersionInfo(Filename, SubBlock) SubBloc= \\ for VS_FIXEDFILEINFO
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return [str(HIWORD(ms)),str(LOWORD(ms)),str(HIWORD(ls)),str(LOWORD(ls))]

        except Exception as e:
            return False,e


class Mac:
    def __init__(self):
        print 'In Mac Constructor'

    def getpath(self):
        print 'In Mac->getpath()'


class OSUtils:
    def __init__(self):
        print 'In OSUtils Constructor'
        if os.name == 'nt':
            self.OSObj = Windows()
        elif os.name == 'posix':
            self.OSObj = Linux()

    def getpath(self):
        print 'In OSUtils->getpath()'
        return self.OSObj.getpath()

    def common(self):
        print 'In OSUtuls->common()'

    def p_GetFileVersion(self,fname):
        return self.OSObj.p_GetFileVersion(fname)


osObj = OSUtils()

osObj.common()
print osObj.getpath()
print osObj.p_GetFileVersion("C:\Program Files\Internet Explorer\iexplore.exe")