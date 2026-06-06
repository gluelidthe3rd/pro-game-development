import pygame
import random
from pygame.locals import*
import time
pygame.init()
screen= pygame.display.set_mode((600,600))
score=0
clock=pygame.time.Clock()
font=pygame.font.SysFont("arial",30)
text=font.render("score:"+str(score),True,"black")
starttime=time.time()

def changebg(image):
    bg=pygame.image.load("IMAGES\\"+image)
    bg1=pygame.transform.scale(bg,(600,600))
    screen.blit(bg1,(0,0))
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("IMAGES\\bin.png")  
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()  
class Recycle(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image=pygame.image.load("IMAGES\\"+image)  
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()  
class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("IMAGES\\pbag.png")  
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()  
images=["bag.png","pencil.png","box.png"]
item_list=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
plastics=pygame.sprite.Group()
for i in range(40):
    items=Recycle(random.choice(images))
    items.rect.x=random.randrange(600)
    items.rect.y=random.randrange(600)
    item_list.add(items)
    all_sprites.add(items)
for i in range(10):
    items=Nonrecycle()
    items.rect.x=random.randrange(600)
    items.rect.y=random.randrange(600)
    plastics.add(items)
    all_sprites.add(items)
bin=Bin()
all_sprites.add(bin)
run = True
while run:
    clock.tick(30)
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    time_elapsed=time.time()-starttime
    if time_elapsed >=60:
        if score >35:
            changebg("win.jpg")
        else:
            changebg("lose.jpg")
    else:
        changebg("background1.png")
        countdown=font.render("timeleft:"+str(60-int(time_elapsed)),True,"black")
        screen.blit(countdown,(30,30))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if bin.rect.y>0:
                bin.rect.y-=5 
        if keys[pygame.K_s]:
            if bin.rect.y<530:
                bin.rect.y+=5
        if keys[pygame.K_d]:
            if bin.rect.x<530:
                bin.rect.x+=5
        if keys[pygame.K_a]:
            if bin.rect.x>0:
                bin.rect.x-=5
        all_sprites.draw(screen)
    pygame.display.update()