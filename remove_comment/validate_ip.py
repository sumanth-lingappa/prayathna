import socket


ip_addr = [
    '1.1.1.1',
    '0.0.0.0',
    '255.255.255.255',
    '300.1.1.1',
    '256.3.3.3'
]

for ip in ip_addr:
    try:
        print 'validating ip {} -->>'.format(ip)
        print socket.inet_aton(ip)
        print '{} is a valid IP'.format(ip)
    except socket.error as er:
        print er
        print '{} is NOT a valid IP'.format(ip)
    print ''
