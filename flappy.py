import pgzrun
import random

WIDTH=800
HEIGHT=600

gravity = 2000.0

class Ball():
    def __init__(self,color,x,y,rad):
        self.c = color
        self.x = x
        self.y = y
        self.r = rad
        self.vx = 200
        self.vy = 0
    def draw(self):
        pos = ( self.x,self.y)
        screen.draw.filled_circle(pos,self.r,self.c)

ball = Ball("blue",400,300,50)
def draw():
    screen.clear()
    ball.draw()

def update(dt):
    uy = ball.vy
    ball.vy+= gravity*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    if ball.y >HEIGHT-ball.r:
        ball.y=HEIGHT-ball.r
        ball.vy=-ball.vy*0.9
    if ball.y < ball.r:
        ball.y= ball.r
        ball.vy = - ball.vy
    ball.x+=ball.vx*dt
    if ball.x >WIDTH-ball.r or ball.x<ball.r:
        ball.vx=-ball.vx
def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500



pgzrun.go()
