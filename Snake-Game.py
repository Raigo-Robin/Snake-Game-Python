import pygame
import time
import random
import sys #0 ei saanud game_close ajal akent kinni panna ülevalt, lisasin selle ja eemaldasin mõned üleliigsed read ja lisasin mõned ka
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
oranž = (255, 105, 30)

dis_width = 600  #full screeni ei saa panna(breakib foodi)
dis_height = 600 
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game Version: 0.1.1')
 
clock = pygame.time.Clock()
 
snake_block = 15 #muutes seda suurust saad muuta mänguväljaku suurust, peab jaguma dis_widthi ja dis_heightiga
snake_speed = 10 #kui teed snake_blocki suuremaks, siis probs tahad panna snake speedi alla
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)
 
def Your_score(score):
    value = score_font.render("Skoor: " + str(score), True, oranž)
    dis.blit(value, [0, 0])
    
 
def our_snake(snake_block, snake_list):
    for x in snake_list[:-1]: #9 teeks pea teise värviga prg
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    pygame.draw.rect(dis, yellow, [snake_list[-1][0], snake_list[-1][1], snake_block, snake_block]) #9
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10.6, dis_height / 3])
 
def gameLoop():
    game_over = False
    game_close = False
    
    snake_up = False #3: snake ei saa liikuda vastupidiselt sellele suunale, kust ta tuli ja sellega end tappa, 
    snake_down = False #3 aga prg sellega veel kerge bug: kui liigud kindlas suunas ja vajutad kahte kindlat klahvi 
    snake_left = False #3 samal ajal, siis võid end ikka ära tappa nt(oled vähemalt 3 pikkune, liigud vasakule ja vajutad 
    snake_right = False #3 'üles' ja 'paremale' klahvi samal ajal, siis saad surma(kui ajastus on õige))
    if (dis_width / snake_block) % 2 == 0: #7 kui dis_width/snake_block pole paaris siis jääb imelik kõik
        x1 = dis_width / 2
        y1 = dis_height / 2
    else: x1 = dis_width / 2 + snake_block/2 ; y1 = dis_height / 2 + snake_block/2 #7 see parandab selle
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1 #snake suurust ei saa muuta
    while True: #8 parandab bugi kus food võib alguses spawnida snake sees
        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block #2 oli: dis_width - snake_block) / 10.0) * 10.0, seob neid muutujaid täielikult snake_blockiga
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block #2, #8
        if foodx !=x1 or foody != y1: #8
            break #8
 
    while not game_over:
        
        while game_close == True:
            #dis.fill(blue) #6 imo oleks parem kui taustale jääks snake surma situatsioon
            message("Mäng läbi! Vajuta C-Mängi uuesti või Q-Lahku", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #0
                    pygame.quit() #0
                    sys.exit() #0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #game_over = True #0
                        #game_close = False #0
                        pygame.quit() #0
                        sys.exit() #0
                        
                    if event.key == pygame.K_c:
                        gameLoop()
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                #game_over = True #0
                pygame.quit() #0
                sys.exit() #0
                
            if event.type == pygame.KEYDOWN:
                
                if (event.key == pygame.K_a or  event.key == pygame.K_LEFT) and not snake_right: #1: laseb nooleklahvidega liigutada, #3 
                    x1_change = -snake_block
                    y1_change = 0
                    snake_up = False ; snake_down = False; snake_left = True ; snake_right = False; break #3 #5 Lisasin break, et parandada #3 tekkinud bugi. 
                elif (event.key == pygame.K_d or  event.key == pygame.K_RIGHT) and not snake_left: #1, #3
                    x1_change = snake_block
                    y1_change = 0
                    snake_up = False ; snake_down = False; snake_left = False ; snake_right = True; break #3 #5 Selle tulemusel kui vajutada kahte klahvi korraga
                elif (event.key == pygame.K_w or  event.key == pygame.K_UP) and not snake_down: #1, #3
                    y1_change = -snake_block
                    x1_change = 0
                    snake_up = True ; snake_down = False; snake_left = False ; snake_right = False; break #3, #5 siis registreeritakse neist ainult esimene
                elif (event.key == pygame.K_s or  event.key == pygame.K_DOWN) and not snake_up: #1, #3
                    y1_change = snake_block
                    x1_change = 0
                    snake_up = False ; snake_down = True; snake_left = False ; snake_right = False; break #3, #5
 
        #if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #6 
            #game_close = True #6
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        if x1 == foodx and y1 == foody: #tõstsin uude kohta, et selles frames kus snake sõõb foodi ära, oleks snake asetus loogilisem
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block #2
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block #2
            Length_of_snake += 1
                
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        
        snake_Head_rect = pygame.Rect(x1, y1, snake_block, snake_block) #6
        if snake_Head_rect.left < 0 or snake_Head_rect.right > dis_width or snake_Head_rect.top < 0 or snake_Head_rect.bottom > dis_height: #6
            game_close = True #6
        
        if not game_close: #6
            snake_List.append(snake_Head)
            snake_saba = snake_List[0] #6
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
        
        
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                snake_List.append(snake_saba)
                game_close = True
        
        while True: #4 bug kus food võib spawnida snake sisse
                if [foodx, foody] in snake_List and len(snake_List) != dis_width*dis_height/snake_block**2: #5 kui 'ruudustik' ei ole snake täis ja food on snake sees
                    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block #4
                    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block #4
                else: break #4
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #tõstsin uude kohta, et kui sööb foodi ära, tehakse kohe uus asemele
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
        if len(snake_List) == dis_width*dis_height/snake_block**2: # kui 'ruudustik on snake täis
            game_close = True
 
        if not game_close: pygame.display.update() #6 
        
        clock.tick(snake_speed)
 
    #pygame.quit() #0
    #quit() #0

gameLoop()
