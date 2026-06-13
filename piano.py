import pygame
import random
import time
pygame.init()
screen= pygame.display.set_mode((600,600))
bg = pygame.image.load("IMAGES\\hq720.jpg")
bg1=pygame.transform.scale(bg,(600,600))
font = pygame.font.SysFont("arial",50)
text = font.render("Guess the key",True,"blue")
c = pygame.mixer.Sound("IMAGES\\piano-c_C_major.wav")
d = pygame.mixer.Sound("IMAGES\\piano-d_D_major.wav")
e = pygame.mixer.Sound("IMAGES\\piano-e_E_major.wav")
f = pygame.mixer.Sound("IMAGES\\piano-f_F_major.wav")
g = pygame.mixer.Sound("IMAGES\\piano-g_G#_major.wav")
b = pygame.mixer.Sound("IMAGES\\freesound_community-b6-82017.mp3")
keys= [c,d,e,f,g,b]
key_choice = random.choice(keys)
run= True
while run:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    
    screen.blit(bg1,(0,0))
    screen.blit(text,(150,35))
    for k in range(3):
        key_choice.play()
        time.sleep(k)
    pygame.display.update()
