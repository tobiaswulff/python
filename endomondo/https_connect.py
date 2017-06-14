#!/usr/bin/env python
import http.client, os.path, sys
import urllib.parse, urllib.request

def getCookie():
	global cookie

	cFile = "cookie.txt"
	if not os.path.isfile(cFile):
		print ('Cookie file not found. Exiting.')
		return

	cookieFile = open('cookie.txt', 'r')
	cookie = cookieFile.readlines()

	if not cookie:
		print('Cookie file is empty. Exiting.')
		return

	print('Print from file.')
	print(cookie)

def getUrl():
	# url = 'https://www.endomondo.com/login'
	# req = urllib.request.Request(url)
	# response = urllib.request.urlopen(req)
	# the_page = response.read()

	# print(the_page)
	# #file.write(the_page)
	conn = http.client.HTTPSConnection('www.endomondo.com', 443)
	conn.putrequest('POST', '/')
	conn.endheaders()
	r = conn.getresponse()
	file = open('result','w')
	text = str(r.read())
	file.write(text)
	file.close
	print('Result')
	print(text)

getCookie()
getUrl()




# https://www.endomondo.com/workouts/478557516/3518451#
# https://www.endomondo.com/?wicket:interface=:3:pageContainer:lightboxContainer:lightboxContent:exportPanel:exportGpxLink::IResourceListener::