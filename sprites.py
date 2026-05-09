import pygame
import random

pygame.init()
screen= pygame.display.set_mode((700,500))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("IMAGES\\r.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()#
        self.rect.x = random.randint(0,700)
        self.rect.y = random.randint(0,500)
    def update(self,keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys_pressed[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys_pressed[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if keys_pressed[pygame.K_d]:
            self.rect.move_ip(5,0)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>700:
            self.rect.right=700
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>500:
            self.rect.bottom=500

sprite = pygame.sprite.Group()
for i in range(10):
    player1 = Player()
    sprite.add(player1)
    
run = True
while run:
    i= pygame.event.poll()
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    if i.type == pygame.MOUSEBUTTONDOWN:
        keys_pressed= pygame.key.get_pressed()
        player1.update(keys_pressed)
        screen.blit(pygame.image.load("IMAGES\space1.png"),(0,0))
        sprite.draw(screen)
        pygame.display.update()

    
    
