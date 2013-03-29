'''
Created on 29. mars 2013

@author: Inge
'''
import pygame
from pygame.locals import * 

black = pygame.color.Color("black")
white = pygame.color.Color("white")

class UI():
    playerOneScore = 0
    playerTwoScore = 0
    
    def __init__(self, title, width):
        self.width = width
        
        self.gameFont = pygame.font.SysFont("monospace", 15, bold=True)
        self.headerFont = pygame.font.SysFont("monospace", 25, bold=True)
        self.topBar = pygame.Rect(0, 0, self.width, 50)
        
        self.gameNameLabel = self.headerFont.render(title, 1, white)
        self.playerOneScoreLabel = self.gameFont.render(str(self.playerOneScore), 1, white)
        self.playerTwoScoreLabel = self.gameFont.render(str(self.playerTwoScore), 1, white)
        
    def updateScores(self, p1, p2):
        self.playerOneScore = p1
        self.playerTwoScore = p2
            
    def update(self):
        self.playerOneScoreLabel = self.gameFont.render(str(self.playerOneScore), 1, white)
        self.playerTwoScoreLabel = self.gameFont.render(str(self.playerTwoScore), 1, white)
        
    def draw(self, screen, p1x, p2x):
        pygame.draw.rect(screen, black, self.topBar)
        
        screen.blit(self.playerOneScoreLabel, (p1x - (self.playerOneScoreLabel.get_size()[0] / 2), 18))
        screen.blit(self.playerTwoScoreLabel, (p2x - (self.playerTwoScoreLabel.get_size()[0] / 2), 18))
        screen.blit(self.gameNameLabel, ((self.width / 2) - (self.gameNameLabel.get_size()[0] / 2), 10))