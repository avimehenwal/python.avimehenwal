This post will show how you can make a small and easy-to-use port scanner program
written in Python.

There are many ways of doing this with Python, and I'm going to do it using the
built-in module Socket.
Sockets
The socket module in Python provides access to the BSD socket interface. 

It includes the socket class, for handling the actual data channel, and functions 
for network-related tasks such as converting a server’s name to an address and
formatting data to be sent across the network. Source

Sockets are widely used on the Internet, as they are behind any kind of
network communications done by your computer. 

The INET sockets, account for at least 99% of the sockets in use. 

The web browser’s that you use opens a socket and connects to the web server.

Any network communication goes through a socket.

For more reading about the socket module, please see the official documentation. 
Socket functions
Before we get started with our sample program, let's see some of the socket
functions we are going to use.

sock = socket.socket (socket_family, socket_type)
Syntax for creating a socket

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
Creates a stream socket

AF_INET
Socket Family (here Address Family version 4 or IPv4)

SOCK_STREAM
Socket type TCP connections

SOCK_DGRAM
Socket type UDP connections

gethostbyname("host")
Translate a host name to IPv4 address format

socket.gethostbyname_ex("host")
Translate a host name to IPv4 address format, extended interface

socket.getfqdn("8.8.8.8")
Get the fqdn (fully qualified domain name)

socket.gethostname()
Returns the hostname of the machine..

socket.error
Exception handling




List of available ports  http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
Socket Status Codes List http://msdn.microsoft.com/en-us/library/windows/desktop/ms740668(v=vs.85).aspx

10061 Connection refused.
No connection could be made because the target computer actively refused it. This usually results from trying to connect to a service that is inactive on the foreign host—that is, one with no server application running.