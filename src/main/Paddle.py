'''
Created on 26. mars 2013

@author: Inge 'zeox' Dalby
'''
import pygame
from pygame.locals import * 

class Paddle():
    active = False
    prevY = 0
    x = 0
    y = 0
    
    def __init__(self, texture, x, y, height):
        self.height = height
        self.texture = texture
        self.x = x
        self.y = y
        self.origX = self.x
        self.origY = self.y
        
    def move(self, y):     
        self.y += y
            
    def setCollide(self, topBar):        
        if self.y < self.height/2:
            self.y = topBar.height + 1
            
        if self.y > self.height/2:
            self.y = self.height - (self.texture.get_size()[1] - 1)
    
    def reset(self):
        self.x = self.origX
        self.y = self.origY
        
    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))
        