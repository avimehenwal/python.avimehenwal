==================================
+	   PORT SCANNER 	 +
==================================

FEATURES :
1) Cross platform
2) Remote as well as local host 

IMPROVEMENTS :
1) OOP Structure could be created
2) Ports could be checked in threaded fashion

DEPENDENCIES :
1) Python 2.7 + should be installed


> The socket module in Python provides access to the BSD socket interface. 
> Sockets are widely used on the Internet, as they are behind any kind of network communications done by your computer. 
> The INET sockets, account for at least 99% of the sockets in use. 
> The web browser’s that you use opens a socket and connects to the web server.
> Any network communication goes through a socket.
> Based on inbuilt module


Socket functions
=================================

sock = socket.socket (socket_family, socket_type)
	Syntax for creating a socket

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	Creates a stream socket INET based TCP socket object

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
No connection could be made because the target computer actively refused it.
This usually results from trying to connect to a service that is inactive on the foreign host—that is, one with no server application running.

==============================================
Port scanning types
==============================================

#TCP scanning
The simplest port scanners use the operating system's network functions and is generally the next option to go to when SYN is not a feasible option (described next). Nmap calls this mode connect scan, named after the Unix connect() system call. If a port is open, the operating system completes the TCP three-way handshake, and the port scanner immediately closes the connection to avoid performing a kind of Denial-of-service attack.[3] Otherwise an error code is returned. This scan mode has the advantage that the user does not require special privileges. However, using the OS network functions prevents low-level control, so this scan type is less common. This method is "noisy", particularly if it is a "portsweep": the services can log the sender IP address and Intrusion detection systems can raise an alarm.

#SYN scanning
SYN scan is another form of TCP scanning. Rather than use the operating system's network functions, the port scanner generates raw IP packets itself, and monitors for responses. This scan type is also known as "half-open scanning", because it never actually opens a full TCP connection. The port scanner generates a SYN packet. If the target port is open, it will respond with a SYN-ACK packet. The scanner host responds with a RST packet, closing the connection before the handshake is completed.[3] If the port is closed but unfiltered, the target will instantly respond with a RST packet.
The use of raw networking has several advantages, giving the scanner full control of the packets sent and the timeout for responses, and allowing detailed reporting of the responses. There is debate over which scan is less intrusive on the target host. SYN scan has the advantage that the individual services never actually receive a connection. However, the RST during the handshake can cause problems for some network stacks, in particular simple devices like printers. There are no conclusive arguments either way.

#UDP scanning
UDP scanning is also possible, although there are technical challenges. UDP is a connectionless protocol so there is no equivalent to a TCP SYN packet. However, if a UDP packet is sent to a port that is not open, the system will respond with an ICMP port unreachable message. Most UDP port scanners use this scanning method, and use the absence of a response to infer that a port is open. However, if a port is blocked by a firewall, this method will falsely report that the port is open. If the port unreachable message is blocked, all ports will appear open. This method is also affected by ICMP rate limiting.[4]
An alternative approach is to send application-specific UDP packets, hoping to generate an application layer response. For example, sending a DNS query to port 53 will result in a response, if a DNS server is present. This method is much more reliable at identifying open ports. However, it is limited to scanning ports for which an application specific probe packet is available. Some tools (e.g., nmap) generally have probes for less than 20 UDP services, while some commercial tools (e.g., nessus) have as many as 70. In some cases, a service may be listening on the port, but configured not to respond to the particular probe packet.
To cope with the different limitations of each approach, some scanners offer a hybrid method. For example, using nmap with the -sUV option will start by using the ICMP port unreachable method, marking all ports as either "closed" or "open|filtered". The open|filtered ports are then probed for application responses and marked as "open" if one is received.

#ACK scanning
ACK scanning is one of the more unique scan types, as it does not exactly determine whether the port is open or closed, but whether the port is filtered or unfiltered. This is especially good when attempting to probe for the existence of a firewall and its rulesets. Simple packet filtering will allow established connections (packets with the ACK bit set), whereas a more sophisticated stateful firewall might not.[5]

#Window scanning
Rarely used because of its outdated nature, window scanning is fairly untrustworthy in determining whether a port is opened or closed. It generates the same packet as an ACK scan, but checks whether the window field of the packet has been modified. When the packet reaches its destination, a design flaw attempts to create a window size for the packet if the port is open, flagging the window field of the packet with 1's before it returns to the sender. Using this scanning technique with systems that no longer support this implementation returns 0's for the window field, labeling open ports as closed.[6]

#FIN scanning
Since SYN scans are not surreptitious enough, firewalls are, in general, scanning for and blocking packets in the form of SYN packets.[3] FIN packets are able to pass by firewalls with no modification to its purpose. Closed ports reply to a FIN packet with the appropriate RST packet, whereas open ports ignore the packet on hand. This is typical behavior due to the nature of TCP, and is in some ways an inescapable downfall.[7]

Other scan types[edit]
Some more unusual scan types exist. These have various limitations and are not widely used. Nmap supports most of these.[5]
• X-mas and Null Scan - are similar to FIN scanning, but:[3]
• X-mas sends packets with FIN, URG and PUSH flags turned on like a Christmas tree
• Null sends a packet with no TCP flags set
• Protocol scan - determines what IP level protocols (TCP, UDP, GRE, etc.) are enabled.
• Proxy scan - a proxy (SOCKS or HTTP) is used to perform the scan. The target will see the proxy's IP address as the source. This can also be done using some FTP servers.
• Idle scan - Another method of scanning without revealing one's IP address, taking advantage of the predictable IP ID flaw.
• CatSCAN - Checks ports for erroneous packets.
• ICMP scan - determines if a host responds to ICMP requests, such as echo (ping), netmask, etc.

