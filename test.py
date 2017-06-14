#!/usr/bin/python3
import subprocess

str1 = 'Hello'
str2 = 'World!'

# for x in range(1,10):
	# print (str1 + ' ' + str2)

str3 = subprocess.check_output('sensors', shell=True, universal_newlines=True)
#print (str3, end="")
#print (str3)
fanSpeed1 = str3.split('\n')[23].split()[3]
fanSpeed2 = str3.split('\n')[24].split()[3]
fanSpeed3 = str3.split('\n')[25].split()[3]
fanSpeed4 = str3.split('\n')[26].split()[3]
mbTemp = str3.split('\n')[28].split()[2][1:5]
cpuTemp = str3.split('\n')[29].split()[2][1:5]
# print
# str3.write(3)
str4 = subprocess.check_output('hddtemp /dev/sda', shell=True, universal_newlines=True)
str5 = subprocess.check_output('hddtemp /dev/sdb', shell=True, universal_newlines=True)
str6 = subprocess.check_output('hddtemp /dev/sdc', shell=True, universal_newlines=True)
str7 = subprocess.check_output('hddtemp /dev/sdd', shell=True, universal_newlines=True)
str8 = subprocess.check_output('hddtemp /dev/sde', shell=True, universal_newlines=True)
splitTemp1 = str4.split()
splitTemp2 = str5.split()
splitTemp3 = str6.split()
splitTemp4 = str7.split()
splitTemp5 = str8.split()
#print (str4, end="")
#print (str5, end="")
print ('Disk1\t',splitTemp1[3])
print ('Disk2\t',splitTemp2[3])
print ('Disk3\t',splitTemp3[3])
print ('Disk4\t',splitTemp4[3])
print ('Disk5\t',splitTemp5[3])
print ('CPUFan\t',' ',fanSpeed2,'rpm', sep='')
print ('FanFront',' ',fanSpeed4,'rpm', sep='')
print ('FanTop\t',' ',fanSpeed1,'rpm', sep='')
print ('FanBack\t',' ',fanSpeed3,'rpm', sep='')
print ('MB Temperature\t',mbTemp,'\N{DEGREE SIGN}C', sep='')
print ('CPU Temperature\t',cpuTemp,'\N{DEGREE SIGN}C', sep='')
