#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 80))
m = 'GET / HTTP/1.1\r\nHost: w2.wulffnix.nu\r\n\r\n'
n = 'GET / HTTP/1.0\r\n\r\n'
s.send(n)
data = s.recv(2048)
s.close()
print 'Recived: '
print data
