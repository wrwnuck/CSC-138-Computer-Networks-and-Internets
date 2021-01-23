#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('Listening at port:', serverPort)

while True:
    print ('Ready to server...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #send one HTTP header line
        output = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(output.encode('utf-8'))

        #Send the conent of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.close()
    
    except IOError:
    #Send response message for file not found
        output = 'HTTP/1.1 404 Not Found \n'
        connectionSocket.send(output.encode('utf-8'))
        connectionSocket.close()

#Close client socket
serverSocket.close()