import socket
from _thread import *
import pickle
import pygame
from GameInfo import GameData, PlayerData
import time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
class Server:
    def __init__(self) -> None:
        self.games = {} #int : game
        self.players = 0
        self.conns = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen()
    
    def ReadData(self, addr):
        data = addr.recv(9000*3)
        return pickle.loads(data)

    def SendData(self, addr, data):
        sData = pickle.dumps(data)
        addr.sendall(sData)

    
    def handleConnection(self, conn, addr, g):
        try:
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
            self.SendData(addr, [player,enemy])
            #set spawn info
                
            #While playing game
            while True:
                pos = self.ReadData(addr)
                player.x += pos[0]
                player.turPos = pos[1]
                self.SendData(addr,[player, enemy])
        except Exception as e:
            print(e)
            print("Player Disconnected")
        finally:
            del self.games[g]
            for key in self.games.keys():
                print(key)

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