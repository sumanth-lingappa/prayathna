import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print """Usage: server.py IP_ADDR PORT
    IP_ADDR: IP Address on which server listens to
    PORT: PORT on which server listens to"""
    sys.exit()

addr = (sys.argv[1], int(sys.argv[2]))
print addr

s.bind(addr)
s.listen(5)

while True:
    (c, addr) = s.accept()
    print 'connection is {} with address {}'.format(c, addr)
    c.send('Thank you for connecting')
    c.close()
    
