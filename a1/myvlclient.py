from socket import *

serverName = ''
serverPort = 12000
bufsize = 64

# AF_INET to specify IPv4, SOCK_STREAM to use TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# address is represented by (host, port) tuple
clientSocket.connect((serverName, serverPort))

sentence = input('Input message length, followed by your lowercase sentence:\n')
sentlen = len(sentence)

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(bufsize)
reclen = bufsize
print("From Server: ", modifiedSentence.decode())

while (reclen < sentlen):
    modifiedSentence = clientSocket.recv(bufsize)
    print("From Server: ", modifiedSentence.decode())
    reclen += bufsize


