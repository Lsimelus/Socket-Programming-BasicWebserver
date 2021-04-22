#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start
serverPort = 12000
serverSocket.bind(('127.0.0.1', serverPort ))#socket preared
serverSocket.listen(1)
print ('the web server is up on port:', serverPort)

#Fill in end

while True:
    #Establish the connection 
    print('Ready to serve...') 

    connectionSocket, addr =  serverSocket.accept()#Fill in start

    try:
        message  = connectionSocket.recv(1024)
        message = message.decode()

        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
        connectionSocket.close()