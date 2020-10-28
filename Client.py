import pygame
from Player import Player
from Map import Map
pygame.init()

#window
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Tanks Multiplayer")

run = True
#Background/Map
bg = pygame.image.load(".\\Sprites\\Background.png")
map = Map(".\\Sprites\\FlatMap.png")
def Redraw(p1):
    win.fill((255,255,255))
    win.blit(bg, (0, 0))
    map.draw(win)
    p1.draw(win)
    pygame.display.update()

P1 = Player(".\\Sprites\\RedTank.png", (1000, 150), 50, 25)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Redraw(P1)
    P1.move()
    P1.ground(map)
pygame.quit()
