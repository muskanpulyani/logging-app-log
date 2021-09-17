import socket
import sys
from sh import tail
import time
from _thread import *


def main():
    ThreadCount = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((socket.gethostbyname("0.0.0.0"), 1241))
    except socket.error as e:
        print(str(e))
    s.listen(5)
    #That allow run our Server all the time
    while True:
        clientsocket, address = s.accept()
        print("Connection from has been established")
        start_new_thread(threaded_client, (clientsocket, ))
        ThreadCount += 1
        print(ThreadCount)
    ServerSocket.close()

#for multiple threading. Now multiple client can able to connect to server 
def threaded_client(connection):
   
    for line in tail("-f", sys.argv[1], _iter=True):
        connection.send(bytes(line,"utf-8"))
    connection.close()


if __name__ == "__main__":
    main()