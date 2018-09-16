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
                if ctypes.windll.user32.MessageBoxW(0, "Do you really want to give up?", "Worlds hardest game", 33) == MBOK:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.pos=(player.pos[0],player.pos[1]-2)
            player.update()
        if keys[pygame.K_DOWN]:
            player.pos=(player.pos[0],player.pos[1]+2)
            player.update()
        if keys[pygame.K_LEFT]:
            player.pos=(player.pos[0]-2,player.pos[1])
            player.update()
        if keys[pygame.K_RIGHT]:
            player.pos=(player.pos[0]+2,player.pos[1])
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
        for o in area.obstacles:
            pygame.draw.circle(screen,BLUE,o.pos,o.rad,0)
            pygame.draw.circle(screen,BLACK,o.pos,o.rad,1)
            
        font = pygame.font.SysFont("vinerhanditc", 24)
        text = font.render("Death Counter: %s" %deaths, True, RED) 
        screen.blit(text,(780 - text.get_width(), 20))
        
        pygame.display.update()
        clock.tick(30)
        
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
                if event.key == pygame.K_p:
                    pause=False
                    pygame.mixer.music.unpause()
            if event.type == pygame.QUIT:
                if ctypes.windll.user32.MessageBoxW(0, "Do you really want to give up?", "Worlds hardest game", 33) == MBOK:
                    pygame.quit()
                    quit()
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
MBOK=1
deaths=0
levels=[1]

pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__))+"\..\music\seeingTheFuture.mp3")
pygame.mixer.music.play(-1)

for i in levels:
    area=gamelogic.area(i)
    player=gamelogic.player((area))
    play()
    
pygame.quit()