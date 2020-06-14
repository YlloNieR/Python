#!/usr/bin/python3

import sys #allows us to enter command line arguments, among other things

import socket #allows to look for ports
from datetime import datetime

#Define our target
#python3 scanner.py <ip>
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate a host name to IP4

else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("."*50)
print("Scanning target "+target)
timestart = datetime.now()
print("Time started: "+ str(timestart))
print("."*50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5) #is a float
		result = s.connect_ex((target,port)) #returns error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()

#Add a pretty banner
print("."*50)
timeend = datetime.now()
timedif = timeend-timestart
timedifminutes = timedif.seconds/60
print("Time ended: "+str(timeend))
#print("timedelta value "+str(timedif))
print("Time spend: "+str(round(timedifminutes,2))+" minutes, "+str(timedif.seconds)+" seconds, "+str(timedif.microseconds)+" microseconds")
print("."*50)
