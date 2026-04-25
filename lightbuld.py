import pygame

pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("turn it on")
off = pygame.image.load("IMAGES\\off.png")
on = pygame.image.load("IMAGES\\on.png")
off2=pygame.transform.scale(off,(600,600))
on2=pygame.transform.scale(on,(600,600))

run = True
while run:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False

    mouse_buttons = pygame.mouse.get_pressed()
    screen.fill("red")

    if mouse_buttons[0]:
        screen.blit(on2 , (0,0))
    else:
        screen.blit(off2 , (0,0))

    

    pygame.display.update()