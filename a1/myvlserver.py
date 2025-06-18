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
bytestoread = int(message[0:nbytesforlen])
print(f"Message length: {bytestoread}")

# the sentence = the message minus the length specifier 
sentence = message[nbytesforlen:len(message)]

while True:
    # capitalize and send the 64 bytes received
    capSentence = sentence.upper()
    print(f"Processed: {sentence}")
    cnSocket.send(capSentence.encode())
    sentlen = len(sentence)
    print(f"Message length sent: {sentlen}")

    # bytestoread = length of message remaining
    bytestoread -= sentlen
    
    # only quit processing if we've read the full message length
    if (bytestoread <= 0):
        break

    sentence = cnSocket.recv(bufsize).decode()

cnSocket.close()
print("Connection closed.")

