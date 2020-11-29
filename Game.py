from Player import Player
import socket
class Game:
    def __init__(self) -> None:
        self.conns = [] #hold conn
        self.players = {} #Player's sprites
        self.needsPlayer = True
        self.playersReady = 0
        print("Game created!")
    
    def AddPlayer(self, conn):
        print(f"New connection {conn}")
        self.conns.append(conn)
        playerSprite = ".\\Sprites\\TankUncolored.png"
        spawnPos = (-1, -1)

        if len(self.conns) == 1:
            playerSprite = ".\\Sprites\\BlueTank.png"
            spawnPos = (100, 500)

        elif len(self.conns) == 2:
            playerSprite = ".\\Sprites\\RedTank.png"
            spawnPos = (1820, 500)
            self.needsPlayer = False
    
        self.players[len(self.conns)] = PlayerData(len(self.conns), playerSprite)

    def PlayerReady(self):
        self.playersReady += 1 

    
    def StartGame():
        pass

    def SpawnPlayers(self):
        pass

class PlayerData:
    def __init__(self, pNo, pSprite) -> None:
        self.pNo = pNo
        self.pSprite = pSprite
        self.pos = (100,500) if self.pNo == 1 else (1820, 500)
        self.pSpize = (50, 100)
    
    def UpdatePos(self, pos):
        self.pos = pos



    

