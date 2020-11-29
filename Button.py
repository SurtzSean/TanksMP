import pygame
from _thread import *
class Button:
    def __init__(self, rect, defaultImg, highlightedImg, onClick, params=None) -> None:
        self.rect = rect
        self.default = pygame.image.load(defaultImg)
        self.default = pygame.transform.scale(self.default, (rect.width, rect.height))
        self.highlighted = pygame.image.load(highlightedImg)
        self.highlighted = pygame.transform.scale(self.highlighted, (rect.width, rect.height))
        self.onClick = onClick
        self.params = params
    
    
    def RenderImage(self, win):
        if self.MouseIsTouching():
            pygame.Surface.blit(win, self.highlighted, self.rect)
        else:
            pygame.Surface.blit(win, self.default, self.rect)
    
    def MouseIsTouching(self):
        pos = pygame.mouse.get_pos()
        if self.rect.colliderect(pygame.Rect(pos[0], pos[1], 1, 1)):
            return True
        return False
    
    #Onclick with altered args
    def OnClick(self, params):
        start_new_thread(self.onClick(*params))

    #default OnClick
    def OnClick(self):
        if self.params == None:
            start_new_thread(self.onClick, ())
        else:
            start_new_thread(self.onClick, self.params)
