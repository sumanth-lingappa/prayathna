import re
import os


with open('file.txt','r') as fr:
    flines = fr.readlines()

ipOctet = r'[0-9]|([1-9][0-9]|1[0-9]){2}|2[0-4][0-9]|25[0-5]'
# ipOctet = r'25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]\.' \
#           r'25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]\.' \
#           r'25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]\.' \
#           r'25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]'
new_pattern = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).'+ \
              r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).'+ \
              r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).'+ \
              r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'


ip_content_re = re.compile(new_pattern)
ip_content_re = re.compile(ipOctet)
ip_reg = ipOctet + r'.' + ipOctet + r'.' + ipOctet + r'.' + ipOctet
#ip_reg = r'\d+.\d+.\d+.\d+'
ip_pattern = r'(' + ip_reg + r')'
# ip_pattern = re.compile(ip_reg)
#ip_pattern = r'([0-9]|([1-9][0-9]|1[0-9]{2})|(2[0-4][0-9]|25[0-5]))\.([0-9]|([1-9][0-9]|1[0-9]{2})|(2[0-4][0-9]|25[0-5]))\.([0-9]|([1-9][0-9]|1[0-9]{2})|(2[0-4][0-9]|25[0-5]))\.([0-9]|([1-9][0-9]|1[0-9]{2})|(2[0-4][0-9]|25[0-5]))'
# ip_pattern = ipOctet
print 'pattern -> {}'.format(ip_pattern)

with open('ipfile.txt','w') as ipfw:
    with open('file.txt','r') as fw:
        for line in fw.readlines():
            sObj = ip_content_re.search(line)
            if not sObj: continue
            iplist = sObj.group()
#             print 'string -> {}'.format(line)
#             iplist = re.findall(ip_pattern, line)
            print iplist
            for i in range(len(iplist)):
                ipfw.write(str(iplist[i]) + os.linesep)





