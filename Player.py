import math
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, width, height) -> None:
        pygame.sprite.Sprite.__init__(self)
        
        #0 = looking left, 1 = looking right
        self.direction = 0

        #Spawn Position (x,y) tuple
        self.pos = pygame.math.Vector2(pos)

        #size
        self.width = width
        self.height = height

        #Sprite
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (width, height))

        #Cannon position
        self.cannonDegree = 180
        self.cannonStartX, self.cannonStartY = self.pos.x, self.pos.y + 5
        self.cannonEndX, self.cannonEndY = self.cannonStartX - math.cos(math.radians(self.cannonDegree)) + 30,  self.cannonStartY - math.sin(math.radians(self.cannonDegree)) + 30
        
        #projectile -- Probably should make classes for these
        projectile = None
        projectileForce = 50 #should have slider or something to change force
        projectileWeight = 20

        #hitBox
        self.hitBox = self.image.get_rect()

        #stats
        self.vel = 5
        self.health = 100
    
    #draw tank + cannon
    def draw(self, win):
        self.cannonStartX, self.cannonStartY = self.pos.x + 20, self.pos.y + 5, 
        self.cannonEndX, self.cannonEndY = self.cannonStartX + 10 + math.cos(math.radians(self.cannonDegree)) * 35,  self.cannonStartY + math.sin(math.radians(self.cannonDegree)) * 35
        pygame.draw.line(win, (0, 0, 0), (self.cannonStartX, self.cannonStartY), (self.cannonEndX, self.cannonEndY), 5)
        win.blit(self.image, self.pos)
    
    def move(self):
        keys = pygame.key.get_pressed()

        #move tank
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.direction != 0:
                #self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 0
            self.pos.x -= self.vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.direction != 1:
                #self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 1
            self.pos.x += self.vel
                    
        self.hitBox.x = self.pos.x
        
        #move cannon
        if keys[pygame.K_UP]:
            if self.cannonDegree < 245:
                self.cannonDegree += 1
            
        if keys[pygame.K_DOWN]:
            if self.cannonDegree > 165:
                self.cannonDegree -=1
    
    def fire(self):
        pass
    
    def fall(self):
        self.pos.y += 9
        self.hitBox.y = self.pos.y
    
    def ground(self, map):
        mapRect = map.rect
        if not(self.hitBox.colliderect(mapRect)):
            self.fall()



