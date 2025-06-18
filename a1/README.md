Assignment 1 - Client/server with variable length message

How to run: 
python3 myvlserver.py; python3 myvlclient.py (in separate terminal windows)
In your client terminal, type in the length of the message you want to send followed by the message. (example: 11helloworld!)

The server will process the message 64 bytes at a time and send back the chunks in capitalized form.

Server output examples:

Connection from 127.0.0.1
Message length: 10
Processed: helloworld
Message length sent: 10
Connection closed.

Connection from 127.0.0.1
Message length: 64
Processed: !herigoeirhgoeirghoierghoerighoerihoeirhgoerigoeirhgoiirehgoih
Message length sent: 62
Processed: e!
Message length sent: 2
Connection closed.

Connection from 127.0.0.1
Message length: 62
Processed: !herigoeirhgoeirghoierghoerighoerihoeirhgoigoeirhgoiirehgoihe!
Message length sent: 62
Connection closed.

Connection from 127.0.0.1
Message length: 99
Processed: !ebebebebebebebebebebebebebebebebebebebebebebebebebebebebebebe
Message length sent: 62
Processed: qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq!
Message length sent: 37
Connection closed.

