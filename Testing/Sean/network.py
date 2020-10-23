import socket
from socket import error

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4, Sock_Stream = TCP/IP
        self.hostname = socket.gethostname()
        self.server = socket.gethostbyname(self.hostname)
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos
    
    def connect(self):
        print("connecting")
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except error as e:
            print(e)
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)