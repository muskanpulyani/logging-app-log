# loging-app-log
**Problem Statement**
    Building a Remote tail utility so that end user can able to fetch particular logs of given remote server 

    
**Approach**
    Designed a client server Architecture . Below are the roles of client and server in this<br />
**Directory Structure** <br />
<img width="574" alt="Screenshot 2021-09-18 at 3 21 39 AM 2" src="https://user-images.githubusercontent.com/39254653/133857630-cca308a2-ad07-4435-9809-815991bfc38b.png">


 **Server**<br />
    server are the remote ip whose logs user want to fetch <br />
    create a new socket using the given address and protocol number<br />
    Bind our server to the specified port<br />
    Now Data is continuously pushed/transmitted to the open connection <br />
    fyi ..The server can able to connect multiple clients concurrently 
    
 ```
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
```
  **client**<br />
  client will first create the socket object<br />
  creates conenction with the socket<br />
  Then start reciving the data from the socket<br />
  fyi . client connection will break once the server stop<br />
  ```
    import socket
    import sys

    def main():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostbyname(sys.argv[1]), 1241))
        while True:
            full_msg = ''
            new_msg = True
            msg = s.recv(256)
            if not msg:
                break
            print(msg)
        s.close()

    if __name__ == "__main__":
        main()
```

**Setup and Run the Server**<br />
**Delployment** <br />
<br />










   
