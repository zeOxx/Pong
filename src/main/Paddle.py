'''
Created on 26. mars 2013

@author: Inge 'zeox' Dalby
'''
import pygame
from pygame.locals import * 

class Paddle():
    
    active = False
    x = 0
    y = 0
    
    def __init__(self, texture, x, y, height):
        self.texture = texture
        self.x = x
        self.y = y
        self.origX = self.x
        self.origY = self.y
        
    def move(self, y):
        self.y += y
        
    def reset(self):
        self.x = self.origX
        self.y = self.origY
        
    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))
        