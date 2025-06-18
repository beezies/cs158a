from socket import *

serverName = ''
serverPort = 12000
bufsize = 64

# AF_INET to specify IPv4, SOCK_STREAM to use TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# address is represented by (host, port) tuple
clientSocket.connect((serverName, serverPort))

# take user input and send to server
sentence = input('Input message length, followed by your lowercase sentence:\n')
sentlen = len(sentence)
clientSocket.send(sentence.encode())

# receive the 64 byte server response
modifiedSentence = clientSocket.recv(bufsize)
reclen = bufsize
print("From Server: ", modifiedSentence.decode())

# if the sent message was longer than the 64-byte bufsuze, continue accepting until the full modified message is received
while (reclen < sentlen):
    modifiedSentence = clientSocket.recv(bufsize)
    print("From Server: ", modifiedSentence.decode())
    reclen += bufsize


