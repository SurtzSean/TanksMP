import socket
from _thread import *
import pickle
import pygame
from Game import Game

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
    
    def handleConnection(self, conn, addr, g):
        print(f"Handling connection {conn}")
        initialData = []
        game = self.games[g]
        game.AddPlayer(conn)
        pNo = len(game.players)
        player = self.games[g].players[pNo]
        initialData.append(player)
        initialData.append(game)
        sendData = pickle.dumps(initialData)
        addr.sendall(sendData)
        while game.needsPlayer:
            sendData = pickle.dumps(game.needsPlayer)
            addr.send(sendData)
        enemyPlayer = game.players[((pNo + 1) % len(game.players)) + 1]
        enemyData = pickle.dumps(enemyPlayer)
        addr.sendall(enemyData)
        ready = False
        #while players are loading in environment
        while not ready:
            try:
                data = addr.recv(9000 * 3)
                readyStatus = pickle.loads(data)
                print(readyStatus)
                if readyStatus == "ready":
                    game.PlayerReady()
                    ready = True
                print("not ready")
            except:
                print("client not ready")
        print("games loaded")
        #waiting for players to load scene this probably doesn't matter in this case but idk
        while game.playersReady != 2:
            gameReady = pickle.loads(False)
            addr.sendall(gameReady)

        addr.sendall(pickle.loads(True))
        
        #Both players are ready, start game
        while True:
            data = addr.recv(9000*3)
            positionInfo = pickle.loads(data)
            player.UpdatePos(positionInfo[0], positionInfo[1])
            userPositions = pickle.dumps(((player.pos),(enemyPlayer.pos)))
            addr.sendall(userPositions)

            
        del self.games[g]

    def connect(self):
        while True:
            addr, conn = self.s.accept()
            g = -1

            for game in self.games.keys(): #Check for another game
                if self.games[game].needsPlayer:
                    g = game
            print(g)
            if g == -1: #If no avaliable game, make one
                try:
                    g = list(self.games.keys())[-1] + 1
                except:
                    g = 0
                self.games[g] = Game()
            try:
                start_new_thread(self.handleConnection, (conn, addr, g))
            except error as e:
                print(e)

s = Server()
s.connect()
