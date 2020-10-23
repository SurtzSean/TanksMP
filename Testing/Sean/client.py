import pygame
from pygame import color

WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow(win, ground, player):
    win.fill((255,255,255))
    player.draw(win)
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
    



def main():
    run = True
    p = Player(50,50,25,25,(0,255,0))
    g = Ground(0,450,WIDTH,50, (0,0,0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        g.checkGrounded(p)
        redrawWindow(win, g, p)

if __name__ == "__main__":
    main()