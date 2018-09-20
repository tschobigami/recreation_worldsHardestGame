import pygame
import gamelogic
import ctypes
import os

def play():
    global deaths
    finished=False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                giveUp()
            if event.type == pygame.KEYDOWN:
                if event.key == PAUSE:
                    pause()
        keys=pygame.key.get_pressed()
        if keys[UP]:
            player.pos=(player.pos[0],player.pos[1]-p_speed)
            player.update()
        if keys[DOWN]:
            player.pos=(player.pos[0],player.pos[1]+p_speed)
            player.update()
        if keys[LEFT]:
            player.pos=(player.pos[0]-p_speed,player.pos[1])
            player.update()
        if keys[RIGHT]:
            player.pos=(player.pos[0]+p_speed,player.pos[1])
            player.update()
        
        area.update()
        if player.check_obstacle():
            deaths+=1
            player.reset()
            area.reset()
            
        if player.check_finished():
            finished=True
              
        screen.fill((50,50,100))
        for lrect in area.lightList:
            pygame.draw.polygon(screen,LIGHTGREY,lrect,0)
        for drect in area.darkList:
            pygame.draw.polygon(screen,DARKGREY,drect,0)
        pygame.draw.polygon(screen,GREEN,area.startArea,0)
        pygame.draw.polygon(screen,GREEN,area.finishArea,0)
        pygame.draw.polygon(screen,BLACK,area.playingField,3)
        pygame.draw.polygon(screen,RED,player.area,0)
        pygame.draw.polygon(screen,BLACK,player.area,3)
        for c in area.coins:
            if not c.found:
                pygame.draw.circle(screen,GOLD,c.pos,c.rad,0)
                pygame.draw.circle(screen,BLACK,c.pos,c.rad,1)
        for o in area.obstacles:
            pygame.draw.circle(screen,BLUE,(int(o.pos[0]),int(o.pos[1])),o.rad,0)
            pygame.draw.circle(screen,BLACK,(int(o.pos[0]),int(o.pos[1])),o.rad,1)
            
        font = pygame.font.SysFont("vinerhanditc", 24)
        text = font.render("Death Counter: %s" %deaths, True, RED) 
        screen.blit(text,(780 - text.get_width(), 20))
        text2 = font.render("Level: %s" %levelCurrent, True, RED) 
        screen.blit(text2,(20, 20))
        
        pygame.display.update()
        clock.tick(fps)
        
def pause():
    pygame.mixer.music.pause()
    pause=True
    s = pygame.Surface((800,600))
    s.set_alpha(128)
    s.fill(WHITE)
    screen.blit(s, (0,0))
    font = pygame.font.SysFont("vinerhanditc", 144)
    text = font.render("PAUSED", True, RED) 
    screen.blit(text,(400 - text.get_width() // 2, 300 - text.get_height() // 2))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == PAUSE:
                    pause=False
                    pygame.mixer.music.unpause()
            if event.type == pygame.QUIT:
                giveUp()
        pygame.display.update()
        
def giveUp():
    if ctypes.windll.user32.MessageBoxW(0, "Do you really want to give up?", "Worlds hardest game", 33) == MBOK:
        pygame.quit()
        quit()
        
def intro():
    intro=True
    global menuChoiceCurrent
    while intro:
        screen.fill((50,50,100))
        textList=[]
        font = pygame.font.SysFont("vinerhanditc", 48)
        for i in range(len(menuChoices)):
            textList.append((font.render(menuChoices[i], True, RED),(75, 50+i*100)))
        textList.append((font.render("-", True, RED),(50, 50+menuChoiceCurrent*100)))
        for t in textList:
            screen.blit(t[0],(t[1][0],t[1][1]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                giveUp()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menuChoiceCurrent=(menuChoiceCurrent-1)%len(menuChoices)
                elif event.key == pygame.K_DOWN:
                    menuChoiceCurrent=(menuChoiceCurrent+1)%len(menuChoices)
                elif event.key == pygame.K_RETURN:
                    if(menuChoices[menuChoiceCurrent]=="quit"):
                        giveUp()
                    elif(menuChoices[menuChoiceCurrent]=="play"):
                        intro=False
                    elif(menuChoices[menuChoiceCurrent]=="settings"):
                        textList2=[]
                        for i in range(len(settingsChoices)):
                            textList2.append((font.render(settingsChoices[i], True, RED),(75, 50+i*100)))
                        textList2.append((font.render("-", True, RED),(50, 50+settingsChoiceCurrent*100)))
                        fadeLeft(textList,textList2)
                        settings()
        

        
        pygame.display.update()
        clock.tick(fps)
    
def settings():
    settings=True
    global settingsChoiceCurrent
    while settings:
        screen.fill((50,50,100))
        textList=[]
        font = pygame.font.SysFont("vinerhanditc", 48)
        for i in range(len(settingsChoices)):
            textList.append((font.render(settingsChoices[i], True, RED),(75, 50+i*100)))
        textList.append((font.render("-", True, RED),(50, 50+settingsChoiceCurrent*100)))
        for t in textList:
            screen.blit(t[0],(t[1][0],t[1][1]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                giveUp()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    settingsChoiceCurrent=(settingsChoiceCurrent-1)%len(settingsChoices)
                elif event.key == pygame.K_DOWN:
                    settingsChoiceCurrent=(settingsChoiceCurrent+1)%len(settingsChoices)
                elif event.key == pygame.K_ESCAPE:
                    settings=False
                elif event.key == pygame.K_RETURN:
                    changeSetting(settingsChoices[settingsChoiceCurrent])
        pygame.display.update()
        clock.tick(fps)
        
def changeSetting(setting):
    changing=True
    while changing:
        screen.fill((50,50,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                giveUp()
        pygame.display.update()
        clock.tick(fps)
        
def fadeLeft(textOutList,textInList):
    global f_speed
    max_length = max([t[0].get_width()+t[1][0] for t in textOutList]+[800-t[1][0] for t in textInList])
    for i in range(round(max_length/f_speed)+1):
        screen.fill((50,50,100))
        for t in textOutList:
            screen.blit(t[0],(t[1][0]-i*f_speed,t[1][1]))
        for t in textInList:
            screen.blit(t[0],(t[1][0]+(round(max_length/f_speed)-i)*f_speed,t[1][1]))
        pygame.display.update()
    

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Worlds hardest game")
clock = pygame.time.Clock()
LIGHTGREY=(180,180,180)
DARKGREY=(90,90,90)
GREEN=(100,200,100)
BLACK=(0,0,0)
RED=(222,0,0)
BLUE=(100,100,200)
WHITE=(255,255,255)
GOLD=(218,165,32)
UP=pygame.K_UP
DOWN=pygame.K_DOWN
LEFT=pygame.K_LEFT
RIGHT=pygame.K_RIGHT
PAUSE=pygame.K_p
MBOK=1
HIGHFPS=60
NORMALFPS=30
HARD=180
fps=NORMALFPS
p_speed=60/fps
f_speed=90/fps
deaths=0
levels=[1,2,3]
levelCounter=-1
levelCurrent=levels[levelCounter]
menuChoices=["play","settings","level editor", "quit"]
menuChoiceCurrent=0
settingsChoices=["fps","keys"]
settingsChoiceCurrent=0

intro()

pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__))+"\..\music\seeingTheFuture.mp3")
pygame.mixer.music.play(-1)

for i in levels:
    levelCounter+=1
    levelCurrent=levels[levelCounter]
    area=gamelogic.area(i,fps)
    player=gamelogic.player((area))
    play()
    
pygame.quit()
quit()