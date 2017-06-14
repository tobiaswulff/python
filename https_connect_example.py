#!/usr/bin/env python

import urllib.request
import requests
from urllib.request import Request, urlopen

url = 'https://www.endomondo.com/login'
url2 = 'http://www.wulffnix.nu'
headers = {'User-Agent':'Mozilla 10.1'}
# url.add_header('User-Agent', 'Mozilla 10.1')

r = urllib.request.urlopen(url)
q = requests.get(url)
# cont = r.read().decode("utf-8")
# url = r.geturl()
# code = r.code
# head = q.headers()

# print(cont)
# print(url)
# print(code)
# print(head)
print(q.headers['Content-Type'])
# for keys, values in q.headers['Content-Type']:
# 	print (keys)
# 	print (values)
