import pygame
class Map(pygame.sprite.Sprite):
    def __init__(self, sprite) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 955
    
    def draw(self, win):
        win.blit(self.image, (0,955))
        
