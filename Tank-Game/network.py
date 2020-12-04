import socket
import pickle
from socket import error

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000

class Network:
    def __init__(self) -> None:
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (HOST, PORT)
        self.c.connect(self.addr)
    
    def ReadData(self):
        data = self.c.recv(9000*3)
        try:
            result = pickle.loads(data)
            return result
        except:
            print("Could not read data")
    
    def SendData(self, data):
        send = pickle.dumps(data)
        try:
            self.c.sendall(send)
        except:
            print("could not send data")

        
    def SendData(self):
        data = "ready"
        sendData = pickle.dumps(data)
        self.c.send(sendData)