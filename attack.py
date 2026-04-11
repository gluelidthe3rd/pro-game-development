import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
w=900
h=500
border = pygame.Rect(w//2-5,0,10,h)
screen= pygame.display.set_mode((w,h))
pygame.display.set_caption("space")
R = "red"
W = "white"
B = "black"
Y = "yellow"

font = pygame.font.SysFont("arial",40)
fps = 60
vel = 5
bullet_vel = 7
max_bullet =3
ssw,ssh=55,40

yellow_hit = pygame.USEREVENT+1
red_hit = pygame.USEREVENT+2

y_img = pygame.image.load("IMAGES\\ye.png")
y_ss = pygame.transform.rotate(pygame.transform.scale(y_img,(ssw,ssh)),90)

r_img = pygame.image.load("IMAGES\\re.png")
r_ss = pygame.transform.rotate(pygame.transform.scale(r_img,(ssw,ssh)),270)

space1 =pygame.transform.scale(pygame.image.load("IMAGES\space1.png"),(w,h))
def draw(red,yellow,r_bullet,y_bullet,r_health,y_health):
    screen.blit(space1,(0,0))
    pygame.draw.rect(screen,B,border)
    r_health_text = font.render("health"+str(r_health),1,W)
    y_health_text = font.render("health"+str(y_health),1,W)
    screen.blit(r_health_text,(w-r_health_text.get_width()-20,10))
    screen.blit(y_health_text,(10,10))
    screen.blit(y_ss,(yellow.x,yellow.y))
    screen.blit(r_ss,(red.x,red.y))
    pygame.display.update()
def y_move(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]and yellow.x-vel>0:
        yellow.x-=vel
    if keys_pressed[pygame.K_d]and yellow.x+vel+yellow.width<border.x:
        yellow.x+=vel
    if keys_pressed[pygame.K_w]and yellow.y-vel>0:
        yellow.y-=vel
    if keys_pressed[pygame.K_s]and yellow.y+vel+yellow.height<h-15:
        yellow.y+=vel

    
red = pygame.Rect(700,300,ssw,ssh)
yellow = pygame.Rect(100,300,ssw,ssh)
r_bullet = []
y_bullet = []
r_health = 10
y_health = 10
clock =pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run=False
    keys_pressed= pygame.key.get_pressed()
    y_move(keys_pressed,yellow)
    draw(red,yellow,r_bullet,y_bullet,r_health,y_health)
    