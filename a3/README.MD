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

~/CS158A/a3> p3 myleprocess.py  
Process uuid: 6d99eaa7-53d1-42c4-89cc-b45fd242ef6c  
Server listening on (127.0.0.1 : 12000)  
Server socket at (localhost : 12001) isn't ready. Retrying..  
Server socket at (localhost : 12001) isn't ready. Retrying..  
Server socket at (localhost : 12001) isn't ready. Retrying..  
Server socket at (localhost : 12001) isn't ready. Retrying..  
Connected to neighbor server (localhost : 12001)  
New connection from (127.0.0.1 : 49361)  
Electing leader...  
Leader is 6d99eaa7-53d1-42c4-89cc-b45fd242ef6c (me!!)  

~/CS158A/a3> cat log1.txt 
Sent: uuid=6d99eaa7-53d1-42c4-89cc-b45fd242ef6c, flag=0  
Recieved: uuid=187ff849-a969-4bca-8051-a5ecfb3e4486, flag=0, less  
IGNORING  
Recieved: uuid=6d99eaa7-53d1-42c4-89cc-b45fd242ef6c, flag=0, equal  
Leader is decided to 6d99eaa7-53d1-42c4-89cc-b45fd242ef6c.  
IM LEADER!!!  
Sent: uuid=6d99eaa7-53d1-42c4-89cc-b45fd242ef6c, flag=1  
Leader: 6d99eaa7-53d1-42c4-89cc-b45fd242ef6c  

By the time all 3 members terminate, the leader will be unanimously agreed upon.

