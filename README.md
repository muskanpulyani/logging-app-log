# loging-app-log
**Problem Statement**
    Building a Remote tail utility so that end user can able to fetch particular logs of given remote server 

    
**Approach**
    Designed a client server Architecture . Below are the roles of client and server <br />
    
**Directory Structure** <br />
<img width="336" alt="Screenshot 2021-09-18 at 3 55 55 AM" src="https://user-images.githubusercontent.com/39254653/133859937-c666c556-9547-4863-b519-8f0ff8578bb7.png">



 **Server**<br />
    server are the remote ip whose logs end user needs to fetch <br />
    create a new socket using the given address and protocol number<br />
    Bind the server to the specified port<br />
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
**Deployment** <br />
**server**<br />
Run ansible script to setup server<br />
user: user to login to remote machine eg .ubuntu/ec2-user/centos<br />
file_name: repersent the log file eg. /var/log/syslog<br />
x.x.x.x : repersent the remote ip
```
ansible-playbook -i x.x.x.x, logging.yml --private-key private_key_path  -u user -e file_name=file_path
```
**Ansible Script do**<br />
Clone the code to /opt directory<br />
Creates a virualenv and install the requirments.txt<br />
Create systemd service remote_log which will continously transmit logs to particular socket.<br />
<img width="1065" alt="Screenshot 2021-09-18 at 3 54 30 AM" src="https://user-images.githubusercontent.com/39254653/133860288-da8deb5e-04b1-41e2-9ecb-93882aa75749.png">
<br />
**Client**<br />
client will run .py file with remote ip address which will we passed as argument 
```
python3 logging-app-log/client/client.py x.x.x.x
```

**client1 reciving system  logs from server **
<img width="1277" alt="Screenshot 2021-09-18 at 2 07 43 PM" src="https://user-images.githubusercontent.com/39254653/133882675-f7ede1cd-530c-453e-9636-545304ffbaa7.png">
**
client2 reciving system  logs from server**
<img width="1278" alt="Screenshot 2021-09-18 at 2 07 33 PM" src="https://user-images.githubusercontent.com/39254653/133882704-e66c6acf-faa4-4d0e-8ad5-3ea80380e376.png">


**server establish two conenctions** 
<img width="775" alt="Screenshot 2021-09-18 at 2 07 58 PM" src="https://user-images.githubusercontent.com/39254653/133882714-73d38494-315c-4d9c-aca5-3e23cc3bd588.png">
