import socket
import pickle
from socket import error

HOST = "50.116.57.17"
PORT = 5000

class Network:
    def __init__(self) -> None:
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (HOST, PORT)
        self.c.connect(self.addr)
    
    def ReadData(self):
        data = self.c.recv(12000)
        try:
            result = pickle.loads(data)
            return result
        except error as e:
            print(e)
    
    def SendData(self, data):
        send = pickle.dumps(data)
        try:
            self.c.sendall(send)
        except:
            print("could not send data")