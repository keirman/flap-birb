import pygame, sys
from pygame.locals import *
import random



def main():
    pygame.init()
    
    x = 100
    y = 100
    pipex = 600
    velocity = 0
    acceleration = 0.1
    pipespeed = -5
    randompipehight = 300
    gameover = 0
    

    DISPLAY=pygame.display.set_mode((600,480),0,34)

    pipes = []

    WHITE=(255,255,255)
    BLUE=(0,0,244)
    RED=(255,0,0)
    GREEN=(0,255,0)

    random.randrange(1,4)
    random.getstate

    pygame.draw.rect(DISPLAY,BLUE,(x,y,100,50))
    while True:
        if y <= -100:
            y =  -100
        if y >= 500:
            gameover = 1

        
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if gameover == 1:  
                        print(gameover)
                    else:
                        velocity = -3
                        print(y)
                if event.key == pygame.K_r:
                    gameover = 0
                    x = 100
                    y = 100
                    pipex = 600
                    velocity = 0
                        

            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        if pipex < -10:
            pipex = 710
        DISPLAY.fill((255,255,255))
        player = pygame.draw.rect(DISPLAY,BLUE,(x,y,45,45))
        if gameover == 0:
            y += velocity
        velocity += acceleration
        if gameover == 0: 
            pipex += pipespeed
        #bottom pipe
        pipe = pygame.draw.rect(DISPLAY,RED,(pipex,randompipehight,50,400))
        #top pipe
        pipe2 = pygame.draw.rect(DISPLAY,RED,(pipex,randompipehight - 540,50,400))
        
        if player.colliderect(pipe2) or player.colliderect(pipe):
            gameover = 1

        pygame.display.update()
        pygame.time.delay(10)

        
        

main()