import pygame
from pygame import Rect
from Globals import GameState
import Globals
from Button import Button
from Game import Game
from Network import Network
import time
def LookForGame():
    print("clicked")
    Globals.state = GameState.PLAYING

bg = pygame.image.load(".\\Sprites\\MainMenuBG.png")

PlayButton = Button(
                    Rect(Globals.WIDTH/2 - (Globals.WIDTH / 5 / 2),
                    Globals.HEIGHT/2 - (Globals.HEIGHT / 5 / 2), Globals.WIDTH/5, Globals.HEIGHT/5), 
                    ".\\Sprites\\PlayButton.png", 
                    ".\\Sprites\\PlayButtonHighlighted.png",
                    LookForGame
                   )

Globals.buttons.append(PlayButton)
def DrawButtons():
    for button in Globals.buttons:
        button.RenderImage(Globals.win)

def DrawMenu():
    Globals.win.blit(bg, (0,0))
    DrawButtons()
    pygame.display.update()