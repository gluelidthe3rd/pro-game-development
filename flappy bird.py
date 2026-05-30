import pygame
import random
from pygame.locals import*
pygame.init()
w=864
h=936
screen= pygame.display.set_mode((w,h))
groundscroll=0
scrollspeed=4
flying= False
gameover=False
pipegap=150
pipefrecency=1500
lastpipe=pygame.time.get_ticks()-pipefrecency
bg=pygame.image.load("IMAGES\\background.png")
floor=pygame.image.load("IMAGES\\floor.png")
restart=pygame.image.load("IMAGES\\restart.png")
clock = pygame.time.Clock()
fps=60
score=0
passpipe=False
font=pygame.font.SysFont("Arial",25)
def draw_text(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))
def reset():
    pipegroup.empty()
    flappy.rect.x=100
    flappy.rect.y=int(h/2)
    score=0
    return score 
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        action=False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action        
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(1,4):
            img=pygame.image.load(f"IMAGES\\bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.velocity=0
        self.click=False
    def update(self):
        if flying == True:
            self.velocity+=0.5
            if self.velocity>8:
                self.velocity=8
            if self.rect.bottom<768:
                self.rect.y+=int(self.velocity)
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click=True
                self.velocity=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.click=False
            self.counter+=1
            flap_cooldown=5
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.image=self.images[self.index]
            self.image=pygame.transform.rotate(self.images[self.index],self.velocity*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("IMAGES\\pipe.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipegap/2)]
        if pos == -1:
            self.rect.topleft=[x,y+int(pipegap/2)]
    def update(self):
        self.rect.x-=scrollspeed
        if self.rect.right<0:
            self.kill()
pipegroup= pygame.sprite.Group()
birdgroup = pygame.sprite.Group()
flappy = Bird(100,int(h/2))
birdgroup.add(flappy)
button=Button(w//2-50,h//2-100,restart)
run = True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    pipegroup.draw(screen)
    screen.blit(floor,(groundscroll,768))
    if len(pipegroup)>0:
        if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.left and birdgroup.sprites()[0].rect.right<pipegroup.sprites()[0].rect.right and passpipe==False:
            passpipe = True
        if passpipe==True:
            if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.right:
                score+=1
                passpipe=False
    draw_text(str(score),font,"black",int(w/2),50)

    if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False)or flappy.rect.top<0:
        gameover=True
    if flappy.rect.bottom>=768:
        gameover=True
        flying=False
    if gameover==False and flying == True:
        timenow=pygame.time.get_ticks()
        if timenow-lastpipe>pipefrecency:
            pipehieght=random.randint(-100,100)
            bottompipe=Pipe(w,int(h/2)+pipehieght,-1)
            toppipe=Pipe(w,int(h/2)+pipehieght,1)
            pipegroup.add(bottompipe)
            pipegroup.add(toppipe)
            lastpipe=timenow
        pipegroup.update()
        groundscroll-=scrollspeed
        if abs(groundscroll)>35:
            groundscroll = 0
    if gameover==True:
        if button.draw()==True:
            gameover=False
            score=reset()
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
        if i.type==pygame.MOUSEBUTTONDOWN and flying == False and gameover==False:
            flying=True
    pygame.display.update()