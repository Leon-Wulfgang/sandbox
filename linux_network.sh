#!/usr/bin/env bash

# TCP
#   nc = net cat : connect to server, thin wrapper over TCP, OS does TCP
#   string = send to server, browser make strings, OS send TCP
#   printf|nc -> server -> http respond
# UDP
# HTTP
#   Layer         Protocols             Concept
#   Application   HTTP, SSH             URLs, passwords
#   Transport     TCP,  UDP             port number,  sessions
#   Internet      IP                    IP addresses, routes
#   Hardware      wifi, ethernet, DSL   signal strength, access points
# verbs [2/9]
#   GET     read, safe method, 200 ok
#   POST    create, 201 created
#   PUT     update/replace, 404 not found
#   PATCH   partial update/modify, 404
#   DELETE  delete  404
#       HEAD    only ask for head, not body
#       TRACE   echoes back to see if intermediate servers changed anything
#       OPTIONS query for supported HTTP methods of the endpoint
#       CONNECT convert request to TCP/IP tunnel, for HTTPS
# status code
#   200     success get
#   301     success post
#   404     file not found
# ports 16bits, 2bytes
#   80    http
#   22    ssh
#   25    smtp email
#   <=1023  need root
#   max=65535
# IP  8bits,  1byte
#   IPv4 # = 3billion
# submask
#   xxx.xxx.0.0/14  => 18bits mask => 255.252.0.0 => 2**18 = 260k addresses
#   xxx.xxx.xxx.0/24 => 8bit mast => 255.255.255.0 => 2**8 = 255 addresses
# private network RFC1918
#   192.168.0.0/24 => 8bit = 2**8 = 255 addresses
#   default gateway 192.168.0.1
ip addr show # web interfaces:
#   ethernet  eth0
#   wifi      wlan0
#   loopback  lo
#   tunnel
#   virtual machine
ip addr show eth0 # show status of ethernet adapter 0
ip route show default # show default gateway
netstat -nr # show default gateway

sudo lsof -i # list sockets

sudo apt-get update && sudo apt-get upgrade # &&=if left ok run right, update and upgrade all apps
sudo apt-get install netcat-openbsd tcpdump traceroute mtr # install networking tools

ping -c3 8.8.8.8 # ping 8888 3 times
host google.com # query DNS resolver for IP of address
host -t a google.com # get ip address, a-type address
host -t aaaa google.com # google no aaaa
host -t mx udacity.com # udacity mail handlers
dig www.google.com # DNS info including metadata and more script useful
#   TTL time to live, remaining cache life (60s)
sudo tcpdump -n -c5 -i eth0 port 22 # show 5 packages on eth0
traceroute www.udacity.com # show route to uda
mtr www.udacity.com # super trace route
printf 'HEAD / HTTP/1.1\r\nHost: www.udacity.com\r\n\r\n' | nc www.udacity.com 80 # print format http request, pipe and send to uda, got 301
printf 'GET / HTTP/1.1\r\nHost: www.udacity.com\r\n\r\n' | nc www.udacity.com 80 > google.txt # get content from google and save to txt
man nc # see manual of net cat
nc -l 3456 # nc listen to port 3456
nc localhost 3456 # send stuff to 3456, show on both side, plain TCP server
# port not listened to returns RST reset flag
# DNS resolver is built in OS
#   DNS record types
#     AAAA  IPv6
#     CNAME alias, canonical/official name
#     NS    which DNS server has the name

