from httplib import *
site = raw_input("Enter URL: ")
connection = HTTPSConnection(site)
connection.request("GET", "/index.html")
response = connection.getresponse()
print response.status
data = response.read()
print data
