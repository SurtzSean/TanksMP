from typing import overload

display_width = 800
display_height = 600
ground_height = 35
radius = 60

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
        self.cannonBallPos = []
        self.firingPower = -1
    
    def AddPlayer(self):
        self.playerCount += 1
        self.ready = self.playerCount == 2

    def CalculateBallPosition(self, pNo, enemyNo, gun_power, position = None):
        player = self.players[pNo]
        enemy = self.players[enemyNo]
        startingShell = []
        if not position:
            startingShell.append(player.x)
            startingShell.append(player.y)
        else:
            startingShell = position
        if pNo == 0:
            startingShell[0] -= (12 - player.turPos) * 2
        else:
            startingShell[0] += (12 - player.turPos) * 2

        if pNo == 0:
            startingShell[1] += int((((startingShell[0] - player.x) * 0.015 / (gun_power / 50)) ** 2) - (player.turPos + player.turPos / (12 - player.turPos)))
        else:
            startingShell[1] += int((((startingShell[0] - player.x) * 0.015 / (gun_power / 50)) ** 2) - (player.turPos + player.turPos / (12 - player.turPos)))
        damage = 0
        if startingShell[1] > display_height - ground_height or isInside(400, 565, 60, startingShell[0], startingShell[1]):
            #print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            #print("Impact:", hit_x, hit_y)
            if enemy.x + 10 > hit_x > enemy.x - 10:
                damage = 25
            elif enemy.x + 15 > hit_x > enemy.x - 15:
                damage = 18
            elif enemy.x + 25 > hit_x > enemy.x - 25:
                damage = 10
            elif enemy.x + 35 > hit_x > enemy.x - 35:
                damage = 5
            return damage
        else:
            return startingShell

#Credit GeeksForGeeks.org
def isInside(circle_x, circle_y, rad, x, y): 
      
    # Compare radius of circle 
    # with distance of its center 
    # from given point 
    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= rad * rad): 
        return True; 
    else: 
        return False; 
