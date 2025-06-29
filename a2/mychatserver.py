from socket import *
import threading
serverPort = 12000
bufsize = 1024

clients = []
clients_lock = threading.Lock()

def client_listen(cnSocket, addr):
  print(f"New connection from ({addr[0]} : {addr[1]})")
  # use the lock to append a new client to the list
  with clients_lock:
    clients.append(cnSocket)
  # keep receiving messages from the client until they send "exit", broadcast the messages
  while True:
    message = cnSocket.recv(bufsize).decode()
    if (message == "exit"):
      break
    full_message = str(addr[1]) + ": " + message
    print(full_message)
    send_message(cnSocket, addr, full_message)
  # lock the clients list and remove the client after "exit"
  with clients_lock:
    clients.remove(cnSocket)
    cnSocket.close()
    print(f"Connection closed with {addr}")

def send_message(sender, addr, message):
  # use the lock to read through the client list & send the message to every other client
  with clients_lock:
    for client in clients:
      if sender != client:
        client.send(message.encode())

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print(f"Server listening on {serverSocket.getsockname()[0]} : {serverPort}")

threads = []
try:
  while True:
    # accept client connections
    cnSocket, addr = serverSocket.accept()
    # spawn a thread for each
    client_thread = threading.Thread(target=client_listen, args=(cnSocket, addr))
    client_thread.start()

    threads.append(client_thread)
# clean up all the threads when the server gets shut down
except KeyboardInterrupt:
    print("\nShutting down server...")

    serverSocket.close()
    # Join all client threads
    for t in threads:
        t.join()

    print("Shut down complete. Bye!")

