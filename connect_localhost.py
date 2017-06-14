#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'www.endomondo.com'
port = 80

remoteIp = socket.gethostbyname( host )
print(remoteIp)

s.connect((host, 80))
print ('sending...')
m = 'GET / HTTP/1.1\r\nHost: wwww.endomondo.com\r\n\r\n'
n = b'GET / HTTP/1.0\r\n\r\n'
s.sendall(m)
data = s.recv(4096)
reply = data.decode('utf-8')
s.close()
print ('Recived: ')
print (str.encode(reply))
