'''
Created on 26. mars 2013

@author: Inge
'''
import pygame
import Paddle
from pygame.locals import * 

class Player():
    score = 0
    
    def __init__(self, paddle):
        self.paddle = paddle
        
    def move(self, y):
        self.paddle.move(y)
        
    def givePoint(self):
        self.score += 1
        
    def draw(self, screen):
        self.paddle.draw(screen)