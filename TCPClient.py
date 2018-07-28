#!/usr/bin/python3

import socket

#Create socket object
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '192.168.1.104'
host = socket.gethostname()

#The TCP port number of the server
port = 444

#Connect the socket object to (host, port)
clientsocket.connect(('192.168.1.104', port))

#Receiving a message from the server with the maximum of 1024 bytes
message = clientsocket.recv(1024)

#Close the socket
clientsocket.close()

print(message.decode('ascii'))
