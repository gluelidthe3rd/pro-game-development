import pygame
pygame.init()
screen= pygame.display.set_mode((600,600))
run = True
class Circle():
    def __init__(self,color,pos,rad):
        self.screen = screen
        self.c = color
        self.p = pos
        self.r = rad
    def draw(self):
        pygame.draw.circle(self.screen,self.c,self.p,self.r)
c1 = Circle("purple",(200,5),25)
c2 = Circle("orange",(25,146),25)
c3 = Circle("green",(150,225),98)
class Square():
    def __init__(self,color,size):
        self.screen = screen
        self.c = color
        self.s = size
    def draw(self):
        pygame.draw.rect(self.screen,self.c,self.s)
r1 = Square("yellow",(5,5,100,100))
r2= Square("blue",(150,150,5,95))
r3= Square("red",(290,290,176,12))
while run:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
        if i.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            r1.draw()
            r2.draw()
            r3.draw()
            pygame.display.update()
        if i.type==pygame.MOUSEBUTTONUP:
            screen.fill("white")
            c1.draw()
            c2.draw()
            c3.draw()
            pygame.display.update()
    