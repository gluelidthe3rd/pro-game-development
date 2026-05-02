import pygame

pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill("white")
l = pygame.image.load("IMAGES\l.png")
font = pygame.font.SysFont("arial",25)
text= font.render("temple runner",True,"black")
screen.blit(text,(325,100))

screen.blit(l,(100,100))
pygame.display.update()
run = True
while run:
    i = pygame.event.poll()
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    if i.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"black",(pos),15)
        pygame.display.update()
    if i.type == pygame.MOUSEBUTTONUP:
        pos1 = pygame.mouse.get_pos()
        pygame.draw.line(screen,"black",(pos),(pos1),5)
        pygame.draw.circle(screen,"black",(pos1),15)
        pygame.display.update()
    