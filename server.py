import socket
from socket import error
import threading
import sys
hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
port = 5555
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4, Sock_Stream = TCP/IP

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)

def threaded_client(conn):
    print("Sending")
    conn.send("connected".encode(FORMAT))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) #number of bytes to recieve
            reply = data.decode(FORMAT)

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)
            conn.sendall(str.encode(reply))
        except error as e:
            print(e)

while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)
    serverThread = threading.Thread(target=threaded_client, args=(conn,))
    serverThread.start()
