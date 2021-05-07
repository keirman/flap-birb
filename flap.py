import pygame, sys, colorsys, math, time, random
from pygame.locals import *



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
    upsidedowntime = 0
    fliped = 0
    
    screen = pygame.display.set_mode((800, 480))

    pipes = []

    WHITE=(255,255,255)
    BLUE=(0,0,244)
    RED=(255,0,0)
    GREEN=(124,252,0)
    BLACK=(0,0,0)
    
    #name of the game
    pygame.display.set_caption('Flap birb by Keirman')
    
    
    pygame.draw.rect(screen,BLUE,(x,y,100,50), 5)
    while True:
        if y <= 0:
            y =  0
            velocity = 0.1
        if y >= 500:
            gameover = 1

        font = pygame.font.SysFont("comicsansms", 35)
        

        if pipex == 100:
            score += 1
            print(score)
        
        RAINBOW=(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

        if randompipechance == 2:
            Pipecolor = (205,133,63)
            if fliped == 0:
                if pipex == 100:
                    fliped = 1
            else:
                if pipex == 100:
                    fliped = 0        
                    
            if fliped == 1:
                acceleration = -0.1
                jumphight = 3 
                randompipechance = random.randint(1, 9)       
                    

            else:
                acceleration = 0.1
                jumphight = -3
                randompipechance = random.randint(1, 25)   
                
        elif randompipechance == 3:
            Pipecolor = RAINBOW
            if pipex == 100:
                score += 10
        

        else:
            Pipecolor = (218,165,32)
            
            
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.CONTROLLERBUTTONDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.CONTROLLER_BUTTON_A or event.key == pygame.BUTTON_LEFT:
                    if gameover == 1:  
                        print(gameover)
                    else:
                        velocity = jumphight
                        print(y)
                if event.key == pygame.K_r:
                    gameover = 0
                    x = 100
                    y = 100
                    pipex = 690
                    velocity = 0
                    score = 0
                        

            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        if pipex < -35:
            pipex = 810
            randompipehight = random.randint(100, 450) 
            randompipechance = random.randint(1, 5)

        
            
        screen.fill((200,200,250))
        if score >= 25:
            player = pygame.draw.rect(screen,RAINBOW,(x,y, 45, 45))
        else:
            player = pygame.draw.rect(screen,BLUE,(x,y,45,45))
        
        if gameover == 0:
            y += velocity
        velocity += acceleration
        
        if gameover == 0: 
            pipex += pipespeed
        #bottom pipe
        bottompipe = pygame.draw.rect(screen,Pipecolor,(pipex,randompipehight,50,400))
        #top pipe
        toppipe = pygame.draw.rect(screen,Pipecolor,(pipex,randompipehight - 560,50,400))
        
        grass = pygame.draw.rect(screen,GREEN,(x - 100, 445, 10000,150))

        if player.colliderect(toppipe) or player.colliderect(bottompipe) or player.colliderect(grass):
            gameover = 1

        pygame.display.update()
        pygame.time.delay(10)

        
        

main()
