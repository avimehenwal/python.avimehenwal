#!/usr/bin/env python

# AUTHOR  :   AVI MEHENWAL
# DATE    :   25-March-2014
# PURPOSE :   POrt scanning utility

""" ENHANCEMENTS:
- Parallel Threads
- Queue Implementation
- Gevent based greenlets
- SocketStatus to be kept seperate in dict format

"""


from datetime import datetime
import subprocess
import threading
import socket
import sys
import os


# Check the OS
os_name = os.name
platform = sys.platform
print "OS = %s Platform = %s"%(os_name,platform)

# Clear the screen
if os_name == 'nt':
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)

# Ask for input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
print "remoteServerIP : ",remoteServerIP

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()
print t1

# Using the range function to specify ports

def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # returns the socket status code
        result = sock.connect_ex((remoteServerIP, port))
        
        # port_status = sock.connect((remoteServerIP, port))
        # tries to actually connect to server running on port
                
        if result == 0:
            print "Port {}: \t Open".format(port)
        elif result == 10061 :
            print "Port {}: \t Connection Refused by server".format(port)
            
        elif result == 10063 :
            print "Port {}: \t Name too long".format(port)
        elif result == 10013 :
            print "Port {}: \t Permission Denied".format(port)

        else :
            print "Port {}: \t Statu code unregistered [{}]".format(port,result)
            
        sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        # sys.exit()
        return -1

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        return -1

    except socket.error as e:
        print "Couldn't connect to server\n",e
        return -1


for port in range(27000,27020):
    t = threading.Thread(target=port_scan(port))
##    print t.getName()


    
# Checking the time again
t2 = datetime.now()
print t2

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total






# PS
# http://www.artfulcode.net/articles/multi-threading-python/
