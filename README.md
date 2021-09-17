# loging-app-log
**Problem Statement**
    Building a Remote tail utility such that end user can able to fetch particular logs of given remote server 
    
**Approach**
    Designed a client server Architecture . Below are the roles of client and server in this 
    
 **Server**
    server are the remote ip whose logs user want to fetch <br />
    Now create a new socket using the given address family,socket type and protocol number and bind our server to the specified port<br />
    Data is continuously pushed/transmitted to the open connection <br />
    The server can able to connect multiple clients concurrently 
    
    import socket
    import sys
    from sh import tail
    import time
    from _thread import *
    ThreadCount = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((socket.gethostbyname("0.0.0.0"), 1241))
    except socket.error as e:
        print(str(e))
    s.listen(5)

    #Created new Thread
    def threaded_client(connection):
        for line in tail("-f", sys.argv[1], _iter=True):
            connection.send(bytes(line,"utf-8"))
        connection.close()

    #That allow run our Server all the time
    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print("Connection from has been established")
        start_new_thread(threaded_client, (clientsocket, ))
        ThreadCount += 1
        print(ThreadCount)
    ServerSocket.close()
  
    
    
    
    
    
  
    
    
    

    
    
   
