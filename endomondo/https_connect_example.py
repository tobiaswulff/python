#!/usr/bin/env python

import urllib.request
import requests
from urllib.request import Request, urlopen

url = 'https://www.endomondo.com/login'

headers = {'User-Agent':'Mozilla 10.1'}
# url.add_header('User-Agent', 'Mozilla 10.1')

cfile = open('cookie.txt','r')
cookie = cfile.read()
cookies = dict(cookies_are=cookie)
print(cookie,'\n')

r = urllib.request.urlopen(url)
q = requests.get(url, cookies=cookies)
# cont = r.read().decode("utf-8")
# url = r.geturl()
# code = r.code
# head = q.headers()
isCookie = True
for value in q.headers:
	if value == 'set-cookie':
		isCookie = False
	print (value)
if isCookie:
	print ('Cookie ok.')
else:
	print ('Invalid cookie.')

wl = requests.get('https://www.endomondo.com/workouts/list', cookies=cookies)

# print(cont)
# print(url)
# print(code)
# print(head)
print(wl.text)
# for keys, values in q.headers['Content-Type']:
# 	print (keys)
# 	print (values)
