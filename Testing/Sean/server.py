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

s.listen(3)

def read_pos(str):
    str = str.split(",")
    return int(float(str[0])), int(float(str[1]))

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,100), (100,100)]
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode()) #number of bytes to recieve
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                #print("Received: ", reply)
               #print("Sending : ", reply)
            conn.sendall(str.encode(make_pos(reply)))
        except error as e:
            conn.close()
            print(e)

playerCount = 0
while True:
    conn, addr = s.accept()
    print(playerCount)
    print("Connected to : ", addr)
    serverThread = threading.Thread(target=threaded_client, args=(conn, playerCount))
    serverThread.start()
    playerCount += 1
