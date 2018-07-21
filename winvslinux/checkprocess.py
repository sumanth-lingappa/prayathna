# from win32com.client import GetObject
# WMI = GetObject('winmgmts:')
# processes = WMI.InstancesOf('Win32_Process')
# process_list = [(p.Properties_("ProcessID").Value, p.Properties_("Name").Value) for p in processes]
# # print process_list
#
# pdict = {}
# for pr in process_list:
#     key = pr[0]
#     value = str(pr[1])
#     pdict[key] = [value]
#
#
#
#
# import psutil
# plist = psutil.get_process_list()
#
# print '1 . ',len(process_list),len(plist)
#
# print sorted(process_list)
# print '-----------------------------'
# print sorted(plist)
#
# import psutil
# # i=1
# for proc in psutil.process_iter():
#     try:
#         pinfo = proc.as_dict(attrs=['pid', 'name'])
#     except psutil.NoSuchProcess:
#         pass
#     else:
#         key = pinfo['pid']
#         value = str(pinfo['name'])
#         pdict[key].append(value)
#         # print(pinfo['pid']),i
#         # i += 1
#
# for p in pdict.keys():
#     if pdict[p][0] != pdict[p][1]:
#         print pdict[p]


import psutil

process_name = "chrome.exe"
for proc in psutil.process_iter():
    if process_name == proc.name():
        print proc.pid


