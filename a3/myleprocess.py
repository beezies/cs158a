import uuid
import threading 
from socket import *
import json
import time
import logging

# config 
config = open('config.txt', 'r')
my_info = config.readline().strip().split(",")
server_info = config.readline().strip().split(",")
config.close()
bufsize = 1024

# information for this process
my_uuid = str(uuid.uuid4())
my_ip_name = my_info[0]
my_serve_port = int(my_info[1])

# information for neighbor server
server_name = server_info[0]
server_port = int(server_info[1])
connected = False

# leader process to be computed
leader_uuid = ''
leader_is_me = False

# logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='log1.txt', format='%(message)s', filemode='w', level=logging.INFO)

# Message wrapper
class Message():
	def __init__(self, uuid, flag):
		self.uuid = uuid
		self.flag = flag

# Thread wrapper that returns the result of target on join
class ReturningThread(threading.Thread):
	def __init__(self, target, args=()):
		super().__init__(target=target, args=args)
		self._return = None
	def run(self):
		self._return = self._target(*self._args)
	def join(self):
		super().join()
		return self._return

# function to initialize the server socket and wait for client connection
def accept_client(server_socket):
	server_socket.bind((my_ip_name, my_serve_port))
	server_socket.listen(1)
	print(f"Server listening on ({server_socket.getsockname()[0]} : {my_serve_port})")
	cn_socket, client_addr = server_socket.accept()
	print(f"New connection from ({client_addr[0]} : {client_addr[1]})")
	return cn_socket

print(f"Process uuid: {my_uuid}")

# initialize server socket & thread to connect to neighbor client
my_server_socket = socket(AF_INET, SOCK_STREAM)
cn_thread = ReturningThread(target=accept_client, args=(my_server_socket,))
cn_thread.start()

# initialize client socket & connect to neighbor server
while (not connected):
	try: 
		my_client_socket = socket(AF_INET, SOCK_STREAM)
		my_client_socket.connect((server_name, server_port))
		print(f"Connected to neighbor server ({server_name} : {server_port})")
		connected = True
	except:
		print(f"Server socket at ({server_name} : {server_port}) isn't ready. Retrying..")
		time.sleep(1)
		continue

# create message with my uuid & send to server 
init_message = Message(my_uuid, 0)
init_message_json = json.dumps(init_message.__dict__) + "\n"
my_client_socket.send(init_message_json.encode())
logger.info(f"Sent: uuid={my_uuid}, flag=0")

# join client thread and save the socket connection
cn_socket = cn_thread.join()
sock_file = cn_socket.makefile()

print("Electing leader...") 

# finally, start loop of accepting client messages and forwarding them to the server until leader is found
while True:
	message_json = sock_file.readline()
	message_dict = json.loads(message_json)
	sent_uuid = message_dict['uuid']
	flag = message_dict['flag']

	# leader has been found --> forward with flag = 1 & break
	if (flag == 1): 
		logger.info(f"Recieved: uuid={sent_uuid}, flag={message_dict['flag']}, greater")
		logger.info(f"Leader is decided to {sent_uuid}.")
		logger.info("FORWARDING")
		leader_uuid = sent_uuid
		leader_msg =  Message(sent_uuid, 1)
		leader_message_json = json.dumps(leader_msg.__dict__) + "\n"
		my_client_socket.send(leader_message_json.encode())
		logger.info(f"Sent: uuid={sent_uuid}, flag=1")
		break

	# received uuid greater than mine --> forward with flag = 0
	elif (sent_uuid > my_uuid):
		logger.info(f"Recieved: uuid={sent_uuid}, flag={message_dict['flag']}, greater")
		logger.info("FORWARDING")
		my_client_socket.send(message_json.encode())
		logger.info(f"Sent: uuid={sent_uuid}, flag=0")

	# received uuid is mine (i am leader) --> forward with flag = 1 & break
	elif (sent_uuid == my_uuid):
		logger.info(f"Recieved: uuid={sent_uuid}, flag={message_dict['flag']}, equal")
		logger.info(f"Leader is decided to {sent_uuid}.")
		logger.info("IM LEADER!!!")
		leader_is_me = True
		leader_uuid = my_uuid
		new_message = Message(my_uuid, 1)
		new_message_json = json.dumps(new_message.__dict__) + "\n"
		my_client_socket.send(new_message_json.encode())
		logger.info(f"Sent: uuid={my_uuid}, flag=1")
		break

	# received uuid is less than mine --> ignore
	else:
		logger.info(f"Recieved: uuid={sent_uuid}, flag={message_dict['flag']}, less")
		logger.info("IGNORING")

logger.info(f"Leader: {leader_uuid}")
res_msg = f"Leader is {leader_uuid} (me!!)\n" if leader_is_me else f"Leader is {leader_uuid}.\n"
print(res_msg)

sock_file.close()
cn_socket.close()
my_client_socket.close()
my_server_socket.close()
