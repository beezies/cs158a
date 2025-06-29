
Assignment 2 - Chat server with multiple clients

How to run:
$ python3 mychatserver.py
(in another terminal window)
$ python3 mychatclient.py
(open as many clients in different windows as desired)

The server will accept messages from the clients and relay them to the rest.
From a client, type "exit" to disconnect.

Server output example:
Server listening on 127.0.0.1 : 12000
New connection from (127.0.0.1 : 49722)
New connection from (127.0.0.1 : 49723)
49723: hello!
49723: how are you doing?
49722: im good thanks. you?
49723: great!
Connection closed with ('127.0.0.1', 49723)
Connection closed with ('127.0.0.1', 49722)

Client output example:
Connected to chat server. Type 'exit' to leave.
hello!
how are you doing?
49722: im good thanks. you?
great!
exit


