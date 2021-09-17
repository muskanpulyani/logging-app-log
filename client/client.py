import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostbyname("13.127.122.142"), 1241))
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