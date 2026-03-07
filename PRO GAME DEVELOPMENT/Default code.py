import pygame
#initalizing the pygame library so it can work
pygame.init()
#creates screen , bit in brackates show size of screen
screen= pygame.display.set_mode((600,600))
#creates the window, while loop is like draw func
run = True
while run:
    #checks if doing anything on the screen
    for i in pygame.event.get():
        #checks if close down tab
        if i.type ==pygame.QUIT:
            #stops while loop
            run=False
    screen.fill("blue")
    #updates screen
    pygame.display.update()
