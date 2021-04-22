from socket import *
import signal

serverName = ''
serverPort = 12000
message = 'HelloWorld'


clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serveradress = clientSocket.recvfrom(1024) 
print("done")       
clientSocket.close()
    
