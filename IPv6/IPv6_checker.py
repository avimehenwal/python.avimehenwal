# AUTHOR    = Avi Mehenwal
# DATE      = 11th-August-2014
# PURPOSE   = How to detect if a windows machine is running IPV6


import socket

def isIPV6():   
    ipv6 = True
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    except:
        ipv6 = False
    return ipv6


if __name__ == "__main__":
    c = isIPV6()
    print(c)
