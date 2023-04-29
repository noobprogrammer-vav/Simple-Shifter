import pygame,random,time,math
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()

#Colours:
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(70,70,70)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
fire = pygame.Color(255, 125, 0)
water = pygame.Color(210,210,255)
color1 = grey
color2 = white

#Params
x,y = 480,480
run = True
imi = 'C'
Score = 0

#Screen
disp = pygame.display.set_mode((x,y))
pygame.display.set_caption('Fire Or Water')

#ruler
lowx,lowy,lowh,loww =   0,430,10,480
lx,ly,lh,lw =           50,0,480,10
topx,topy,toph,topw =   0,50,10,480
rx, ry,rh,rw =          430,0,480,10
dest = ['l','r','u','d']
color_position = 'l'
cl,cr,cu,cd = fire,fire,fire,fire

#game_over:
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


#water drop:
waterx,watery = 240,240
water_radius = 10
water_speed = 0.1
waterposx,waterposy = 240,240
ini = True
move = 'nil'

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ini:
            move = 'l'
            ini = False
        if keys[pygame.K_RIGHT] and ini:
            move = 'r'
            ini = False
        if keys[pygame.K_UP] and ini:
            move = 'u'
            ini = False
        if keys[pygame.K_DOWN] and ini:
            move = 'd'
            ini = False
    if move == 'l':
        waterx -= water_speed
    elif move == 'r':
        waterx += water_speed
    elif move == 'u':
        watery -= water_speed
    elif move == 'd':
        watery += water_speed
    else:
        continue

    if (waterx > 430 or waterx < 30 or watery > 430 or watery < 30):
        game_over()

    if color_position == move:
        waterx, watery = waterposx, waterposy
        ini = True
        color_position = random.choice(dest)
        Score+=1
        if water_speed < 0.2:
            water_speed += 0.01
    if color_position == 'l':
        cl,cr,cu,cd = water,fire,fire,fire
    elif color_position == 'r':
        cl,cr,cu,cd = fire,water,fire,fire
    elif color_position == 'u':
        cl,cr,cu,cd = fire,fire,water,fire
    elif color_position == 'd':
        cl,cr,cu,cd = fire,fire,fire,water
    disp.fill(white)
    pygame.draw.rect(disp, cu, (topx,topy,topw,toph))
    pygame.draw.rect(disp, cd, (lowx,lowy,loww,lowh))
    pygame.draw.rect(disp, cr, (rx,ry,rw,rh))
    pygame.draw.rect(disp, cl, (lx,ly,lw,lh))
    pygame.draw.circle(disp, water, (waterx,watery), water_radius)
    pygame.display.update()
pygame.quit()
