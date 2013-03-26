'''
Created on 26. mars 2013

@author: Inge 'zeox' Dalby
'''
import pygame
import Paddle
import Player
import Ball
from pygame.locals import * 

WINDOW_TITLE = "Pyng!"
WIDTH = 800
HEIGHT = 600
black = pygame.color.Color("black")
white = pygame.color.Color("white")

class GameMain():
    running = True
    color_bg = Color(50, 50, 50)
    
    def __init__(self, width, height):
        pygame.init()

        # save w, h, and screen
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode(( self.width, self.height ))
        pygame.display.set_caption( WINDOW_TITLE )        
        pygame.key.set_repeat(30,30) 

        # fps clock, limits max fps
        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.fps_max = 60        
        self.initPlayers()
    
    def initPlayers(self):
        self.paddleTexture = pygame.image.load("paddle.png")
        self.ballTexture = pygame.image.load("ball.png")
        self.gameFont = pygame.font.SysFont("monospace", 15, bold=True)
        self.headerFont = pygame.font.SysFont("monospace", 25, bold=True)
        self.topBar = pygame.Rect(0, 0, self.width, 50)
        
        self.ball = Ball.Ball(self.ballTexture, (self.height + self.topBar.height), self.width)
        
        self.paddleSpeed = 15
        self.paddleOneStartX = 80
        self.paddleTwoStartX = self.width - self.paddleOneStartX - self.paddleTexture.get_size()[0]
        self.paddleStartHeight = ((self.height + self.topBar.height)/2) - (self.paddleTexture.get_size()[1] / 2)
        
        self.paddleOne = Paddle.Paddle(self.paddleTexture, self.paddleOneStartX, self.paddleStartHeight, self.height - self.topBar.height)
        self.playerOne = Player.Player(self.paddleOne)
        self.paddleTwo = Paddle.Paddle(self.paddleTexture, self.paddleTwoStartX, self.paddleStartHeight, self.height - self.topBar.height)
        self.playerTwo = Player.Player(self.paddleTwo)
        
        self.gameNameLabel = self.headerFont.render(WINDOW_TITLE, 1, white)
        self.playerOneScore = self.gameFont.render(str(self.playerOne.score), 1, white)
        self.playerTwoScore = self.gameFont.render(str(self.playerTwo.score), 1, white)
        
    def main_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            
            # cap FPS if: limit_fps == True
            if self.limit_fps: 
                self.clock.tick( self.fps_max )
            else: 
                self.clock.tick()
    
    def draw(self):
        self.screen.fill( self.color_bg )
        
        self.playerOne.draw(self.screen)
        self.playerTwo.draw(self.screen)
        
        self.ball.draw(self.screen)
        
        pygame.draw.rect(self.screen, black, self.topBar)
        
        self.screen.blit(self.playerOneScore, (self.playerOne.paddle.x - (self.playerOneScore.get_size()[0] / 2), 15))
        self.screen.blit(self.playerTwoScore, (self.playerTwo.paddle.x - (self.playerTwoScore.get_size()[0] / 2), 15))
        self.screen.blit(self.gameNameLabel, ((self.width / 2) - (self.gameNameLabel.get_size()[0] / 2), 10))
        
        pygame.display.flip()
        
    def update(self):
        self.now = pygame.time.get_ticks()
        
        self.playerOneScore = self.gameFont.render(str(self.playerOne.score), 1, white)
        self.playerTwoScore = self.gameFont.render(str(self.playerTwo.score), 1, white)

    def handle_events(self):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        kmods = pygame.key.get_mods()
        
        for event in events:
            if event.type == pygame.QUIT: 
                self.running = False
                
            # event: keydown
            elif event.type == KEYDOWN:
                if keys[K_ESCAPE]:
                    self.running = False                
                
                #Player 1:
                if keys[K_w]:
                    self.playerOne.move(-self.paddleSpeed)
                if keys[K_s]:
                    self.playerOne.move(self.paddleSpeed)
                    
                #Player 2:
                if keys[K_UP]:
                    self.playerTwo.move(-self.paddleSpeed)
                if keys[K_DOWN]:
                    self.playerTwo.move(self.paddleSpeed)

if __name__ == "__main__":         
    game = GameMain(WIDTH, HEIGHT)
    game.main_loop()    