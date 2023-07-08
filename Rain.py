import pygame,random,time
from pygame.locals import *

pygame.init()

#Colours:
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
fire = pygame.Color(255, 88, 34)
color1 = white
color2 = black
cc = color1

#Params
x,y = 1200,600
run = True
Score = -10

#Screen
disp = pygame.display.set_mode((x,y))
pygame.display.set_caption('Shooter2.O')

#Shooter:
shooter_x = int(x/2.4)
shooter_w,shooter_h = int(x/20),int(y/10)
shooter_y = y-(int(y/6))
shooter_speed = 1
movement = [False,False]
shooter_all_instances = []

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

#Astroids:
Astroid_pos = [i for i in range(1,x,30)]
Astroid_y = y
pos = 0
Astroid_speed = 0.7
border = 5

#Creation:

while run:

    if Astroid_y >= y:
        pos = random.sample(Astroid_pos, 11)
        Astroid_y = 0
        Score+=10
        if Astroid_speed <= 1.6:
            Astroid_speed +=0.2
        if shooter_speed <=2:
            shooter_speed += 1
    Astroid_y+= Astroid_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement[0] = True
            if event.key == pygame.K_RIGHT:
                movement[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movement[0] = False
            if event.key == pygame.K_RIGHT:
                movement[1] = False
        
    if movement[0] == True and shooter_x >= 0:
        shooter_x -= shooter_speed
    if movement[1] == True and shooter_x < (x-shooter_w):
        shooter_x += shooter_speed
    shooter_all_instances.clear()
    for i in range(shooter_x,(shooter_x+shooter_w)):
        shooter_all_instances.append(i)
    if Astroid_y >= shooter_y:
        if (pos[0] in shooter_all_instances or pos[1] in shooter_all_instances or pos[2] in shooter_all_instances or pos[3] in shooter_all_instances or pos[4] in shooter_all_instances):
            game_over()
        if (pos[5] in shooter_all_instances or pos[6] in shooter_all_instances or pos[7] in shooter_all_instances or pos[8] in shooter_all_instances or pos[9] in shooter_all_instances):
            game_over()

    
    disp.fill(color1)
    pygame.draw.rect(disp,color2,(shooter_x, shooter_y, shooter_w, shooter_h))
    pygame.draw.circle(disp, fire, (pos[0],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[1],Astroid_y), 20,border)
    pygame.draw.circle(disp, fire, (pos[2],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[3],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[4],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[5],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[6],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[7],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[8],Astroid_y), 10,border)
    pygame.draw.circle(disp, fire, (pos[9],Astroid_y), 10,border)
    #pygame.draw.circle(disp, fire, (pos[10],Astroid_y), 5,2)
    
    pygame.display.update()

'''
    pygame.draw.circle(disp, blue, (pos[5],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[6],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[7],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[8],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[9],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[10],Astroid_y), 5,2)
    
    pygame.draw.circle(disp, blue, (pos[11],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[12],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[13],Astroid_y), 5,2)
    pygame.draw.circle(disp, blue, (pos[14],Astroid_y), 5,2)
'''