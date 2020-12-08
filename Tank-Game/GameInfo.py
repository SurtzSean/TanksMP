from typing import overload

display_width = 800
display_height = 600
ground_height = 35

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
        self.firing = -1
        self.players = [PlayerData(720, 540, 100, (0,0,255), 0),PlayerData(80, 540, 100, (255,0,0), 0)]
        self.playerCount = 0
        self.turn = 0
    
    def AddPlayer(self):
        self.playerCount += 1
        self.ready = self.playerCount == 2

    def CalculateBallPosition(self, pNo, enemyNo, gun_power):
        player = self.players[pNo]
        enemy = self.players[enemyNo]
        startingShell = []
        startingShell.append(player.x)
        startingShell.append(player.y)
        if pNo == 0:
            startingShell[0] -= (12 - player.turPos) * 2
        else:
            startingShell[0] += (12 - player.turPos) * 2

        if pNo == 0:
            startingShell[1] += int((((startingShell[0] - player.x) * 0.015 / (gun_power / 50)) ** 2) - (player.turPos + player.turPos / (12 - player.turPos)))
        else:
            startingShell[1] -= int((((startingShell[0] - player.x) * 0.015 / (gun_power / 50)) ** 2) - (player.turPos + player.turPos / (12 - player.turPos)))
        damage = 0
        if startingShell[1] > display_height - ground_height:
            #print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            #print("Impact:", hit_x, hit_y)
            if enemy.x + 10 > hit_x > enemy.x - 10:
                print("Critical Hit!")
                damage = 25
            elif enemy.x + 15 > hit_x > enemy.x - 15:
                print("Hard Hit!")
                damage = 18
            elif enemy.x + 25 > hit_x > enemy.x - 25:
                print("Medium Hit")
                damage = 10
            elif enemy.x + 35 > hit_x > enemy.x - 35:
                print("Light Hit")
                damage = 5
            return damage
        else:
            return startingShell

        