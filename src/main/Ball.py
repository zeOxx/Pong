'''
Created on 26. mars 2013

@author: Inge
'''
import pygame
from pygame.locals import * 
from random import randrange

class Ball():
    x = 0
    y = 0
    xSpeed = 4
    ySpeed = 3
    
    def __init__(self, texture, width, height):
        self.texture = texture
        
        self.x = (width / 2) - (self.texture.get_size()[0] / 2)
        self.y = (height / 2) - (self.texture.get_size()[1] / 2)
        
        self.origX = self.x
        self.origY = self.y
        
        self.reset()
        
    def reset(self):
        self.x = self.origX
        self.y = self.origY
        
        #chose random start-direction
        directionX = randrange(2) #0 = left, 1 = right
        directionY = randrange(2) #0 = up, 1 = down
        
        #set the correct updateX interval
        if directionX:
            self.updateX = self.xSpeed
        else:
            self.updateX = -self.xSpeed
            
        #set the correct updateY interval
        if directionY:
            self.updateY = self.ySpeed
        else:
            self.updateY = -self.ySpeed
        
    def update(self):
        self.x += self.updateX
        self.y += self.updateY
        
    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))