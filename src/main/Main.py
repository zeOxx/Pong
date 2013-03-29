'''
Created on 26. mars 2013

@author: Inge 'zeox' Dalby
'''
import pygame
import Paddle
import Player
import Ball
import UI
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
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(( self.width, self.height ))
        pygame.display.set_caption( WINDOW_TITLE )        
        pygame.key.set_repeat(30,30) 

        # fps clock, limits max fps
        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.fps_max = 60        
        self.initGame()
    
    def initGame(self):
        self.ui =  UI.UI(WINDOW_TITLE, self.width)
        
        self.paddleTexture = pygame.image.load("paddle.png")
        self.ballTexture = pygame.image.load("ball.png")
        
        self.ball = Ball.Ball(self.ballTexture, self.width, (self.height + self.ui.topBar.height))
        
        self.paddleSpeed = 15
        self.paddleOneStartX = 80
        self.paddleTwoStartX = self.width - self.paddleOneStartX - self.paddleTexture.get_size()[0]
        self.paddleStartHeight = ((self.height + self.ui.topBar.height)/2) - (self.paddleTexture.get_size()[1] / 2)
        
        self.paddleOne = Paddle.Paddle(self.paddleTexture, self.paddleOneStartX, self.paddleStartHeight, self.height - self.ui.topBar.height)
        self.playerOne = Player.Player(self.paddleOne)
        self.paddleTwo = Paddle.Paddle(self.paddleTexture, self.paddleTwoStartX, self.paddleStartHeight, self.height - self.ui.topBar.height)
        self.playerTwo = Player.Player(self.paddleTwo)
            
    def detectCollision(self):
        #storing paddles and ball in rects
        p1rect = pygame.Rect(self.playerOne.paddle.x, self.playerOne.paddle.y, self.playerOne.paddle.texture.get_size()[0], self.playerOne.paddle.texture.get_size()[1])
        p2rect = pygame.Rect(self.playerTwo.paddle.x, self.playerTwo.paddle.y, self.playerTwo.paddle.texture.get_size()[0], self.playerTwo.paddle.texture.get_size()[1])
        ballRect = pygame.Rect(self.ball.x, self.ball.y, self.ball.texture.get_size()[0], self.ball.texture.get_size()[1])
        
        #checking for ball and player 1 OR ball and player 2
        if p1rect.colliderect(ballRect) or p2rect.colliderect(ballRect):
            self.ball.changeDirection(0)
            
        #check for topbar collision OR maximum height collision
        if self.ui.topBar.colliderect(ballRect) or (ballRect.y + ballRect.height) > self.height:
            self.ball.changeDirection(1)
        
    def reset(self):
        self.ball.reset()
        self.playerOne.reset()
        self.playerTwo.reset()
        
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
        
        self.ui.draw(self.screen, self.playerOne.paddle.x, self.playerTwo.paddle.x)
        
        pygame.display.flip()
        
    def update(self):
        self.now = pygame.time.get_ticks()
        self.detectCollision()
        
        self.ui.update()
        self.ball.update()

    def handle_events(self):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        #kmods = pygame.key.get_mods()
        
        for event in events:
            if event.type == pygame.QUIT: 
                self.running = False
                
            # event: keydown
            elif event.type == KEYDOWN:
                #Exit game
                if keys[K_ESCAPE]:
                    self.running = False
                
                #Reset
                if keys[K_r]:
                    self.reset()
                
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