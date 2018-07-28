#!/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()     # Host is server IP
port = 444                      # The TCP port number this server is bound to

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#listen for incoming connection
serversocket.listen(3)

#Infinite loop, each iteration handles a connection from a client
while True:
    #Accept the connection 
    clientsocket,address = serversocket.accept()

    print("received connection from " % str(address))
    
    #Message sent to client after successful connection
    message = 'hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message)

    clientsocket.close()
