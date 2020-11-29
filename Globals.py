import pygame
from enum import Enum
class GameState(Enum):
    MENU = 1
    PLAYING = 2
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((WIDTH, HEIGHT))
buttons = []
n = None
state = GameState.MENU