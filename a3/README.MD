Assignment 3 - Ring leader election member

Creates a process that can be connected in a ring with other members, each using their own configuration file to initialize the connections. They will then as a group elect a leader process before terminating.

How to run: 
To run a ring locally --
```$ python3 myleprocess.py; python3 myleprocess1.py; python3 myleprocess2.py``` (in separate terminal windows)
To form a ring with other computers -- 
replace the second line in the config.txt file to include the IP and port of the server to your "right", and run 
```$ python3 myleprocess.py```

The results will be saved to the process's respective log.txt file.

Example:

$ python3 myleprocess.py
Process uuid: 30c322d6-d568-4e52-8952-31299ae6a5a9
Server listening on (127.0.0.1 : 12000)
Connected to neighbor server (localhost : 12001)
New connection from (127.0.0.1 : 51334)
Electing leader...
Leader is c08bf1ca-48f3-4288-883f-f2e0c9b227e2.

log1.txt --
Sent: uuid=30c322d6-d568-4e52-8952-31299ae6a5a9, flag=0
Recieved: uuid=c08bf1ca-48f3-4288-883f-f2e0c9b227e2, flag=0, greater
FORWARDING
Sent: uuid=c08bf1ca-48f3-4288-883f-f2e0c9b227e2, flag=0
Recieved: uuid=c08bf1ca-48f3-4288-883f-f2e0c9b227e2, flag=1, greater
Leader is decided to c08bf1ca-48f3-4288-883f-f2e0c9b227e2.
FORWARDING
Sent: uuid=c08bf1ca-48f3-4288-883f-f2e0c9b227e2, flag=1
Leader: c08bf1ca-48f3-4288-883f-f2e0c9b227e2

By the time all 3 members terminate, the leader will be unanimously agreed upon.

