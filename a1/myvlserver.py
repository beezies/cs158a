from socket import *

serverPort = 12000
bufsize = 64
nbytesforlen = 2

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#queue size = 1
serverSocket.listen(1)

# accept client connection
cnSocket, addr = serverSocket.accept()
print(f"Connection from {addr[0]}")

# read first 64 bytes & extract message length
message = cnSocket.recv(bufsize).decode()
msglen = int(message[0:nbytesforlen])
sentence = message[nbytesforlen:len(message)]
print(f"Message length: {msglen}")

while True:

    capSentence = sentence.upper()
    print(f"Processed: {sentence}")

    cnSocket.send(capSentence.encode())
    sentlen = len(sentence)
    print(f"Message length sent: {sentlen}")

    # only quit processing if we've read the full message length
    if (msglen < bufsize):
        break

    sentence = cnSocket.recv(bufsize).decode()
    msglen -= bufsize 

cnSocket.close()
print("Connection closed.")

