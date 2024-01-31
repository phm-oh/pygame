import pygame
import time
import random

pygame.init()

white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0,)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

dis_width = 600
dis_height = 400
# สร้างหน้าจอ
dis = pygame.display.set_mode((dis_width , dis_height))
pygame.display.set_caption('first game on this years by Phanu')

clock = pygame.time.Clock()

my_block = 10
my_speed = 15

font_style = pygame.font.SysFont("bahnschrift" ,25)
score_font = pygame.font.SysFont("comicsansms" , 35)

#ฟั่งชันเพื่อแสดงผล
def Your_score(score):
    value = score_font.render("YOUR SCORE:" + str(score) ,True,yellow)
    dis.blit(value,[0,0])
    
def our_block(my_block, block_list):
    for x in block_list:
        pygame.draw.rect(dis,black,[x[0] ,x[1] , my_block ,my_block ]) 

def message(msg,color):
    mesg =font_style.render(msg,True,color)  
    dis.blit(mesg,dis_width/6 ,dis_height /3)   
    
def gameLoop():
    game_over = False
    game_close = False
    
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0
    
    block_list = []
    lenght_of_block =1 
    
    #สุ่มตำแหน่งของ item
    foodx = round(random.randrange(0,dis_width - my_block )/10.0)*10.0
    foody = round(random.randrange(0, dis_height - my_block) / 10.0) * 10.0

    
    while not game_over:
        while game_close ==True:
            dis.fill(blue)
            message('You Lost! Press C-Play or Q-Quit',red)
            Your_score(lenght_of_block - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -my_block 
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = my_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -my_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = my_block
                    x1_change = 0 
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 :
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)               
        pygame.draw.rect(dis,green,[foodx , foody, my_block ,my_block])               
        my_Head = []
        my_Head.append(x1)
        my_Head.append(y1) 
        block_list.append(my_Head)    
        if len (block_list) > lenght_of_block :
            del block_list[0]    
        for x in block_list[:-1]  :
            if x == my_Head:
                game_close = True 
        
        our_block(my_block , block_list)   
        Your_score(lenght_of_block - 1) 
        pygame.display.update() 
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width - my_block)/10.0) *10.0
            foody = round(random.randrange(0, dis_height - my_block) / 10.0) * 10.0
    
            lenght_of_block += 1               
        clock.tick(my_speed)  
    pygame.quit() 
    quit() 
gameLoop()                   