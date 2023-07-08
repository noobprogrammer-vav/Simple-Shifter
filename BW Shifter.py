import pygame
from pygame.locals import *
import random
import time

pygame.init()

#colours:
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
color = black
colorx = white

#Params:
x,y = 480,480
imi = 'L'
Score = 0

#Screen:
pygame.display.set_caption("Shift game")
disp = pygame.display.set_mode((x,y))


#Box at Left:
Bo_x,Bo_y = int(x/6),y-int(y/6) #Box at Right:  int(x/1.5)

#Separator:
separator = pygame.Rect(int(x/2),0,1,y+10)

#Bullet:
Bl_x = [int(x/4.4),int(x/1.4)]
Bl_y = int(y/24)
Bullet_speed = 10
Bullet_position = Bl_x[0]

#Game Over:
def game_over():
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render('Game Over!! Your Score is : ' + str(Score), True, red)       
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (x/2, y/2)
    disp.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    print(Score)
    time.sleep(5)
    running = False
    pygame.quit()
    
#logic and animation
running = True
while running:
    pygame.time.delay(100)
    
    Bl_y += Bullet_speed
    if Bl_y >= y:
        Bl_y = int(y/24)
        Score += 1
        if Bullet_speed <= 90:
            Bullet_speed += 3
        if random.randint(0, 1) == 0:
            Bullet_position = Bl_x[0]
        else:
            Bullet_position = Bl_x[1]
    
    if Bullet_position == Bl_x[0] and imi == 'L' and (Bl_y-Bullet_speed) > (y - int(y/4.5)):
        game_over()
    if Bullet_position == Bl_x[1] and imi == 'R' and (Bl_y-Bullet_speed) > (y - int(y/4.5)):
        game_over()

    if running != False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                Bo_x = int(x/6)
                imi = 'L'
                colorx = white
                color = black

            if keys[pygame.K_RIGHT]:
                Bo_x = int(x/1.5)
                imi = 'R'
                colorx = black
                color = white
        
    disp.fill(colorx)
    pygame.draw.rect(disp,color,(Bullet_position,Bl_y,int(x/24),int(y/24)),2)
    pygame.draw.rect(disp,color,separator)
    pygame.draw.rect(disp,color,(Bo_x,Bo_y,int(x/6),int(y/6)))
    pygame.display.update()