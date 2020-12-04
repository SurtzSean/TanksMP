from typing import overload


class PlayerData:
    def __init__(self, x, y, playerHealth, playerColor, turPos = 0) -> None:
        self.x = x
        self.y = y
        self.health = playerHealth
        self.color = playerColor
        self.turPos = turPos

class GameData:
    def __init__(self) -> None:
        self.ready = False
        self.players = {}
        self.playerCount = 0
    
    def AddPlayer(self):
        pInfo = PlayerData(0,0,0,0,0)
        if self.playerCount == 0:
            pInfo = PlayerData(720, 540, 100, (0,0,255), 0)
        else:
            pInfo = PlayerData(80, 540, 100, (255,0,0), 0)
        self.playerCount += 1
        self.players[self.playerCount] = pInfo
        self.ready = self.playerCount == 2