import pygame
from pygame.locals import*
import time

pygame.init() 
screen= pygame.display.set_mode((600,600)) 
s = pygame.image.load("IMAGES\\s.png")
r = pygame.image.load("IMAGES\\r.png")
r_x= 200
r_y= 200
keys=[False,False,False,False]
while r_y<600: 
    screen.blit(s,(0,0))
    screen.blit(r,(r_x,r_y))
    #for locals use flip
    pygame.display.flip()    
    for i in pygame.event.get():        
        if i.type ==pygame.QUIT:
            pygame.quit()
        if i.type== pygame.KEYDOWN:
            if i.key==K_UP:
                keys[0]=True
            elif i.key==K_DOWN:
                keys[1]=True
            elif i.key==K_LEFT:
                keys[2]=True
            elif i.key==K_RIGHT:
                keys[3]=True
        if i.type== pygame.KEYUP:
            if i.key==K_UP:
                keys[0]= False
            elif i.key==K_DOWN:
                keys[1]= False
            elif i.key==K_LEFT:
                keys[2]= False
            elif i.key==K_RIGHT:
                keys[3]= False
    if keys[0]:
        if r_y>0:
            r_y-=7.5
    if keys[1]:
        if r_y<530:
            r_y+=7.5
    if keys[2]:
        if r_x>0:
            r_x-=7.5
    if keys[3]:
        if r_x<530:
            r_x+=7.5
    r_y+=5
    time.sleep(0.05)
print("gameover!")

    
    
    