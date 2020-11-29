import pygame
from pygame import Rect, error
from Player import Player
from Globals import GameState
import Globals
from Map import Map
from Button import Button
from Game import Game, PlayerData
import MainMenu
from Network import Network
from _thread import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Tanks Multiplayer")

def WaitToStart():
    needsPlayer = True
    while needsPlayer:
        try:
            needsPlayer = n.ReadData()
        except:
            needsPlayer = True
            print("missed data")
        CheckEvents()

def CheckEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Globals.buttons:
                if button.MouseIsTouching():
                    button.OnClick()

    

run = True
while run:
    CheckEvents()
    if Globals.state == GameState.MENU:
        MainMenu.DrawMenu()
    elif Globals.state == GameState.PLAYING:
        try:
            n = Network()
            data = n.ReadData()
            game = data[1]
            pData = data[0]
            player = Player(pData.pSprite, pData.pos, pData.pSpize[0], pData.pSpize[1])
            print("started")
            WaitToStart()
            print("starting")
            enemy = n.ReadData()
            enemy = Player(enemy.pSprite, enemy.pos, enemy.pSize[0], enemy.pSize[1])

            bg = pygame.image.load(".\\Sprites\\Background.png")
            Globals.win.blit(bg, (0,0))
            print("sending data")
            n.SendData("ready")
            print("data sent")
            gameReady = False
            while not gameReady:
                CheckEvents()
                try:
                    data = n.ReadData()
                    gameReady = data
                except:
                    gameReady = False
            while True:
                n.SendData((player.pos.x, player.pos.y))
                positions = n.ReadData()
                playerPos, enemyPos = positions[0], positions[1]
                player.pos = (playerPos[0], playerPos[1])
                enemy.pos = (enemyPos[0], enemyPos[1])
                player.draw(Globals.win)
                enemy.draw(Globals.win)
                pygame.display.update()
                player.move()
                CheckEvents()
                
            
        except error as e:
            Globals.state == GameState.MENU
            print(e)


pygame.quit()
