import pygame

pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill("white")
l = pygame.image.load("IMAGES\\l.png")
b= pygame.image.load("IMAGES\\su.png")
y= pygame.image.load("IMAGES\\cc.jpg")
z= pygame.image.load("IMAGES\\t.png")
font = pygame.font.SysFont("arial",25)
text= font.render("temple runner",True,"black")
text1= font.render("subway surfers",True,"black")
text2= font.render("ludo",True,"black")
text3= font.render("candy crush",True,"black")
toptext= font.render("Match the games up!",True,"black")
screen.blit(text,(325,100))
screen.blit(text1,(325,200))
screen.blit(text2,(325,300))
screen.blit(text3,(325,400))
screen.blit(toptext,(150,50))
screen.blit(l,(100,100))
screen.blit(y,(100,200))
screen.blit(b,(100,300))
screen.blit(z,(100,400))
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
    