import pygame
import time
import random
from tkinter import *

    
gs=0    
def themaingame(gid,ll):
    global gs
    pygame.init()
     
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    blue = (153, 0, 153)
    
    green = (0, 255, 0)
     
    w = 600
    h = 400
     
    dis = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Snake Game')
     
    clock = pygame.time.Clock()
     
    sb = 10
    ss = 15
     
    fs = pygame.font.SysFont("bahnschrift", 25)
    sf = pygame.font.SysFont("comicsansms", 35)
     
     
    def sco(score):
        value = sf.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])
     
     
     
    def ts(sb, sl):
        for x in sl:
            pygame.draw.rect(dis, black, [x[0], x[1], sb, sb])
     
     
    def message(msg, color):
        mesg = fs.render(msg, True, color)
        dis.blit(mesg, [w / 6, h / 3])
     
     
    def gameLoop():
        global gs
        gover = False
        gclose = False
     
        xa = w / 2
        ya = h / 2
     
        xac = 0
        yac = 0
     
        sl = []
        lens = 1
     
        fx = round(random.randrange(0, w - sb) / 10.0) * 10.0
        fy = round(random.randrange(0, h - sb) / 10.0) * 10.0
     
        while not gover:
     
            while gclose == True:
                dis.fill(blue)
                message("You Lost! press Q-Quit", red)
                sco(lens - 1)
                
                pygame.display.update()
                
     
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_q:
                            gover = True
                            gclose = False
                            gs=lens - 1
            if ll==1:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        gover = True
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_LEFT:
                            xac = -sb
                            yac = 0
                        elif ev.key == pygame.K_RIGHT:
                            xac = sb
                            yac = 0
                        elif ev.key == pygame.K_UP:
                            yac = -sb
                            xac = 0
                        elif ev.key == pygame.K_DOWN:
                            yac = sb
                            xac = 0
                        elif ev.key == pygame.K_m:
                            lens+=5
                        elif ev.key == pygame.K_n:
                            gs+=5
                        
            if ll==0:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        gover = True
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_a:
                            xac = -sb
                            yac = 0
                        elif ev.key == pygame.K_d:
                            xac = sb
                            yac = 0
                        elif ev.key == pygame.K_w:
                            yac = -sb
                            xac = 0
                        elif ev.key == pygame.K_s:
                            yac = sb
                            xac = 0
                        elif ev.key == pygame.K_m:
                            lens+=5
                        elif ev.key == pygame.K_n:
                            gs+=5
         
            if xa >= w or xa < 0 or ya >= h or ya < 0:
                gclose = True
            xa += xac
            ya += yac
            dis.fill(blue)
            pygame.draw.rect(dis, green, [fx, fy, sb, sb])
            sh = []
            sh.append(xa)
            sh.append(ya)
            sl.append(sh)
            if len(sl) > lens:
                del sl[0]
     
            for x in sl[:-1]:
                if x == sh:
                    gclose = True
     
            ts(sb, sl)
            sco(lens - 1)
     
            pygame.display.update()
     
            if xa == fx and ya == fy:
                fx = round(random.randrange(0, w - sb) / 10.0) * 10.0
                fy = round(random.randrange(0, h - sb) / 10.0) * 10.0
                lens += 1
     
            clock.tick(ss)
        pygame.quit()
        gs=lens-1
    
    gameLoop()
    return(gs,gid)

    

