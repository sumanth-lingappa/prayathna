import socket
import sys

BUF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print """Usage: client.py IP_ADDR PORT
    IP_ADDR and PORT of the server to which client connects to"""
    sys.exit()

s = socket.socket()

addr = (sys.argv[1], int(sys.argv[2]))

s.connect(addr)

print s.recv(BUF_SIZE)

s.close()
