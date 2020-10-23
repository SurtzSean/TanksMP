from network import Network
import pygame
from pygame import color

WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow(win, ground, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    ground.draw(win)
    pygame.display.update()

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = .25
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def fall(self):
        self.y += self.vel

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if(self.x > 0):
                self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            if self.x < (WIDTH - self.width):
                self.x += self.vel
        if keys[pygame.K_UP]:
            if self.y > 0:
                self.y -= self.vel
        if keys[pygame.K_DOWN]:
            if self.y < (HEIGHT - self.height):
                self.y += self.vel

        self.update()
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

class Ground():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def checkGrounded(self, player):
        if((player.y + player.height) < self.y):
            player.fall()
        elif((player.y + player.height) > self.y):
            player.y = self.y - player.height

def read_pos(pos):
    pos = pos.split(",")
    return int(pos[0]), int(pos[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])



def main():
    run = True
    print("not connected")
    n = Network()
    print("connecting")
    startPos = read_pos(n.getPos())
    p1 = Player(startPos[0],startPos[1],25,25,(0,255,0))
    p2 = Player(startPos[0],startPos[1],25,25,(0,0,255))

    g = Ground(0,450,WIDTH,50, (0,0,0))

    while run:
        print("connecting")
        p2Pos = read_pos(n.send(make_pos((p1.x, p1.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move()
        g.checkGrounded(p1)
        redrawWindow(win, g, p1, p2)

if __name__ == "__main__":
    main()