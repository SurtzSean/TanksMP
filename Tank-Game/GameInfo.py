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
        self.players = [PlayerData(720, 540, 100, (0,0,255), 0),PlayerData(80, 540, 100, (255,0,0), 0)]
        self.playerCount = 0
    
    def AddPlayer(self):
        self.playerCount += 1
        self.ready = self.playerCount == 2
    
    def CheckHit(self, tank, hit_x):
        damage = 0
        if tank.x + 10 > hit_x > tank.x - 10:
            print("Critical Hit!")
            damage = 25
        elif tank.x + 15 > hit_x > tank.x - 15:
            print("Hard Hit!")
            damage = 18
        elif tank.x + 25 > hit_x > tank.x - 25:
            print("Medium Hit")
            damage = 10
        elif tank.x + 35 > hit_x > tank.x - 35:
            print("Light Hit")
            damage = 5
        return damage
        