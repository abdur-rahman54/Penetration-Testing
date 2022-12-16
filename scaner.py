#!/bin/python3

import sys #allows us to enter command line argument
import socket 
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate a host name to IPV4
else:
	print("Invalid maount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("_" * 50)

try :
	for port in range (50,1000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		results = s.connect_ex((target,port)) #return error indicator
		print("Checking port {}.".format(port))
		if results == 0:
			print("Port {} is open.".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldnt connet to server")
	sys.exit()
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
