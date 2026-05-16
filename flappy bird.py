import pygame
from pygame.locals import*
pygame.init()
w=864
h=936
screen= pygame.display.set_mode((w,h))
groundscroll=0
scrollspeed=4
bg=pygame.image.load("IMAGES\\background.png")
floor=pygame.image.load("IMAGES\\floor.png")
clock = pygame.time.Clock()
fps=60
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
    def update(self):
        self.counter+=1
        flap_cooldown=5
        if self.counter>flap_cooldown:
            self.counter=0
            self.index+=1
            if self.index>=len(self.images):
                self.index=0
        self.image=self.images[self.index]
birdgroup = pygame.sprite.Group()
flappy = Bird(100,int(h/2))
birdgroup.add(flappy)
run = True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    screen.blit(floor,(groundscroll,768))
    groundscroll-=scrollspeed
    if abs(groundscroll)>35:
        groundscroll = 0
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    pygame.display.update()