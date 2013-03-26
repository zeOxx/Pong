'''
Created on 26. mars 2013

@author: Inge
'''
import pygame
from pygame.locals import * 

class Ball():
    x = 0
    y = 0
    
    def __init__(self, texture, width, height):
        self.texture = texture
        
        # The code below does not work as intended. I have no idea why
        self.x = (width / 2) - (self.texture.get_size()[0] / 2)
        self.y = (height / 2) - (self.texture.get_size()[1] / 2)
        
        self.origX = self.x
        self.origY = self.y
        
    def reset(self):
        self.x = self.origX
        self.y = self.origY
        
    #def update(self):
        #do shit
        
    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))