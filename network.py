import socket
import pickle
import struct
from socket import error

HOST = "localhost"
PORT = 5000

class Network:

    def __init__(self) -> None:
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (HOST, PORT)
        self.c.connect(self.addr)
    
    def send_msg(self, msg):
        # Prefix each message with a 4-byte length (network byte order)
        msg = struct.pack('>I', len(msg)) + msg
        self.c.sendall(msg)

    def recv_msg(self):
        # Read message length and unpack it into an integer
        raw_msglen = self.recvall(4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        # Read the message data
        return self.recvall(msglen)

    def recvall(self, n):
        # Helper function to recv n bytes or return None if EOF is hit
        data = bytearray()
        while len(data) < n:
            packet = self.c.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data

    def ReadData(self):
        data = self.recv_msg()
        try:
            result = pickle.loads(data)
            return result
        except error as e:
            print(e)
    
    def SendData(self, data):
        send = pickle.dumps(data)
        try:
            self.send_msg(send)
        except:
            print("could not send data")