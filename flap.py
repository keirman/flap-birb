import pygame, sys, colorsys, math, time 
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
    randompipechance = 1
    Pipecolor = 1
    score = 0
    jumphight = -3
    
    screen = pygame.display.set_mode((800, 480))

    pipes = []

    WHITE=(255,255,255)
    BLUE=(0,0,244)
    RED=(255,0,0)
    GREEN=(30,245,10)
    BLACK=(0,0,0)
    
    #name of the game
    pygame.display.set_caption('Flap birb by Keirman')
    
    
    pygame.draw.rect(screen,BLUE,(x,y,100,50))
    while True:
        if y <= -40:
            y =  0
        if y >= 500:
            gameover = 1

        font = pygame.font.SysFont("comicsansms", 35)

        

        if randompipechance == 2:
            Pipecolor = (255,164,0)
            acceleration = -0.1
            jumphight = 3

        else:
            Pipecolor = (255,0,0)
            
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if gameover == 1:  
                        print(gameover)
                    else:
                        velocity = jumphight
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

        if pipex < -35:
            pipex = 810
            randompipehight = random.randint(100, 500) 
            randompipechance = random.randint(1, 25)
            score += 1
            
        screen.fill((200,200,250))
        player = pygame.draw.rect(screen,BLUE,(x,y,45,45))
        grass = pygame.draw.rect(screen,GREEN,(x - 100, 445, 10000,150))
        if gameover == 0:
            y += velocity
        velocity += acceleration
        print(velocity)
        if gameover == 0: 
            pipex += pipespeed
        #bottom pipe
        pipe = pygame.draw.rect(screen,Pipecolor,(pipex,randompipehight,50,400))
        #top pipe
        pipe2 = pygame.draw.rect(screen,Pipecolor,(pipex,randompipehight - 560,50,400))
        
        
        if player.colliderect(pipe2) or player.colliderect(pipe) or player.colliderect(grass):
            gameover = 1

        pygame.display.update()
        pygame.time.delay(10)

        
        

main()
