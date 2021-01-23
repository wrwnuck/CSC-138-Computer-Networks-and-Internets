from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com' #Fill in start #Fill in end
port = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
#Fill in end

recv = clientSocket.recv(1024).decode()
print("recv: ", recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("recv1: ", recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# OPTIONAL: Establish secure connection TLS
startTLSCommand = "STARTTLS\r\n"
clientSocket.send(startTLSCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print("recv2: ", recv2)
if recv2[:3] != '220':
    print('220 reply not received from server.')
tlsClientSocket = ssl.wrap_socket(clientSocket)

tlsClientSocket.send(heloCommand.encode())
recv3 = tlsClientSocket.recv(1024).decode()
print("recv3: ", recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

authLoginCommand = 'AUTH LOGIN\r\n'
tlsClientSocket.send(authLoginCommand.encode())
recv4 = tlsClientSocket.recv(1024).decode()
print("recv4: ", recv4)
if recv4[:3] != '334':
    print('334 reply not received from server.')

tlsClientSocket.send(base64.b64encode(("testfor472hw1@gmail.com").encode()))
tlsClientSocket.send(('\r\n').encode())
recv5 = tlsClientSocket.recv(1024).decode()
print("recv5: ", recv5)
if recv5[:3] != "334":
    print('334 reply not received from server.')

tlsClientSocket.send(base64.b64encode(("tedu1234").encode()))
tlsClientSocket.send(('\r\n').encode())
recv6 = tlsClientSocket.recv(1024).decode()
print("recv6: ", recv6)
if recv6[:3] != "235":
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM:<testfor472hw1@gmail.com>\r\n'
tlsClientSocket.send(mailFromCommand.encode())
recv7 = tlsClientSocket.recv(1024).decode()
print("recv7: ", recv7)
if recv7[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = 'RCPT TO:<wrwnuck@gmail.com>\r\n'
tlsClientSocket.send(rcptToCommand.encode())
recv8 = tlsClientSocket.recv(1024).decode()
print("recv8: ", recv8)
if recv8[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
tlsClientSocket.send(dataCommand.encode())
recv9 = tlsClientSocket.recv(1024).decode()
print("recv9: ", recv9)
if recv9[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
tlsClientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
tlsClientSocket.send(endmsg.encode())
recv10 = tlsClientSocket.recv(1024).decode()
print("recv10: ", recv10)
if recv10[:3] != "250":
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
tlsClientSocket.send(quitCommand.encode())
recv11 = tlsClientSocket.recv(1024).decode()
print("recv11: ", recv11)
if recv11[:3] != '221':
    print('221 reply not received from server.')
# Fill in end