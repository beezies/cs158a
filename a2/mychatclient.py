from socket import *
import threading

serverName = 'localhost'
serverPort = 12000
bufsize = 1024

def send_messages(socket):
    while True:
        sendmessage = input("")
        socket.send(sendmessage.encode())
        if (sendmessage == "exit"):
            socket.close()
            break

def receive_messages(socket):
    while True:
        try:
            servermessage = socket.recv(bufsize).decode()
            print(servermessage)
        except: 
            break

# AF_INET to specify IPv4, SOCK_STREAM to use TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# address is represented by (host, port) tuple
clientSocket.connect((serverName, serverPort))
print("Connected to chat server. Type 'exit' to leave.")

# to enable simultaneous message sending/receiving, use a thread for each
send_thread = threading.Thread(target=send_messages, args=(clientSocket,))
receive_thread = threading.Thread(target=receive_messages, args=(clientSocket,))
send_thread.start()
receive_thread.start()

send_thread.join()
receive_thread.join()



