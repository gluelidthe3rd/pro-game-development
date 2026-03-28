import pygame
import time 

pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("Alles Gute zum Geburtstag")
Bild = pygame.image.load("IMAGES\\BDAY.jpg")
Bild1=pygame.transform.scale(Bild,(600,600))

run = True
while run:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    screen.fill("blue")
    screen.blit(Bild1,(0,0))
    font =pygame.font.SysFont("arial",25)
    text = font.render("Wishing you a happy birthday!",True,"black")
    screen.blit(text,(150,300))
    pygame.display.update()
    time.sleep(2)
    Kuchen = pygame.image.load("IMAGES\\CAKE.jpg")
    Kuchen1 = pygame.transform.scale(Kuchen,(600,600))
    screen.blit(Kuchen1,(0,0))
    pygame.display.update()
    time.sleep(2)
