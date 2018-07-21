"""
extract all IPs in a log file and put them into a list
"""
import re

filename = "log_file.csv"
file = open(filename,'r')
# for line in file:
#     print line

lines = file.readlines()
ValidIpAddressRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

validIPRegex = r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"

iprange = r'([0-9]\.[0-9]\.[0-9]\.[0-9]){4}'

ip2 = r'([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)'
# import socket
# socket.inet_aton(ip)

pattern = validIPRegex
# pattern = '[0-9]'
for line in lines:
    string = str(line)
    m = re.search(pattern,string)
    if m:
        print m.group()