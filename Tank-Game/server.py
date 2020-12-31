import socket
from _thread import *
import pickle
import pygame
import struct
from GameInfo import GameData, PlayerData
import time

HOST = 'localhost'
PORT = 5000

class Server: 
    def __init__(self) -> None:
        self.games = {} #int : game
        self.players = 0
        self.conns = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen()

    def recvall(self,addr, n):
        # Helper function to recv n bytes or return None if EOF is hit
        data = bytearray()
        while len(data) < n:
            packet = addr.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data

    def send_msg(self, addr, msg):
        # Prefix each message with a 4-byte length (network byte order)
        msg = struct.pack('>I', len(msg)) + msg
        addr.sendall(msg)

    def recv_msg(self,addr):
        # Read message length and unpack it into an integer
        raw_msglen = self.recvall(addr,4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        # Read the message data
        return self.recvall(addr,msglen)
    
    def ReadData(self,addr):
        data = self.recv_msg(addr)
        return pickle.loads(data)

    def SendData(self, addr, data):
        sData = pickle.dumps(data)
        self.send_msg(addr,sData)
    
    def handleConnection(self, conn, addr, g):
        try:
            clock = pygame.time.Clock()
            game : GameData = self.games[g]
            game.AddPlayer()
            pNo = game.playerCount % 2
            player = game.players[pNo]
            enemyNo = (pNo + 1) % 2
            enemy = game.players[enemyNo]
            print("test")
            #Wait for player
            while not game.ready:
                self.SendData(addr, "WaitingForPlayer")
            self.SendData(addr, "Ready")
            print("Ready")
            self.SendData(addr, [player,enemy, pNo])
            #While playing game
            while True:
                pos = self.ReadData(addr)
                if game.turn == pNo and type(pos) == type([1,]) and pos[0] == "Firing":
                    game.firing = pNo
                    if pos[1] > 100:
                        game.firingPower = 100
                    elif pos[1] < 1:
                        game.firing = 1
                    else:
                        game.firingPower = pos[1]
                if game.firing != -1:
                    self.SendData(addr, "FIRING")
                    power = game.firingPower
                    defenderNo = (game.firing + 1) % 2
                    val = game.CalculateBallPosition(game.firing, defenderNo, power)
                    if pNo != defenderNo:
                        while type(val) != type(1): #while it is returning coordiantes
                            game.cannonBallPos = val
                            self.SendData(addr, game.cannonBallPos)
                            val = game.CalculateBallPosition(game.firing, defenderNo, power, game.cannonBallPos)
                            clock.tick(60)
                        game.turn = defenderNo
                        game.firing = -1
                        game.players[defenderNo].health -= val
                    else:
                        while game.firing != -1:
                            print(game.cannonBallPos)
                            self.SendData(addr, game.cannonBallPos)
                            clock.tick(60)
                    self.SendData(addr, "HIT")
                elif game.turn == pNo:
                    if player.x + pos[0] < 800 and player.x + pos[0] > 1 and (player.x + pos[0] > 480 or player.x + pos[0] < 320):
                        player.x += pos[0]
                    player.turPos = pos[1]
                self.SendData(addr,[player, enemy])
                clock.tick(60)
        except error as e:
            print(e)
        finally:
            if self.games[g]:
                del self.games[g]

    def connect(self):
        while True:
            addr, conn = self.s.accept()
            g = -1

            for game in self.games.keys(): #Check for another game
                if not self.games[game].ready:
                    g = game
            print(g)
            if g == -1: #If no avaliable game, make one
                try:
                    g = list(self.games.keys())[-1] + 1
                except:
                    g = 0
                self.games[g] = GameData()
            try:
                start_new_thread(self.handleConnection, (conn, addr, g))
            except error as e:
                print(e)

blue = (0,0,255)
red = (200, 0, 0)

s = Server()
s.connect()