# e2.3DrawPython.py
from turtle import *
def drawSnake(radius, angle, length):
    seth(-40)
    for i in range(length):
        circle(radius, angle)
        circle(-radius, angle)
    circle(radius, angle/2)
    fd(40)
    circle(16, 180)
    fd(40* 2/3)
setup(650, 350, 200, 200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
drawSnake(40, 80, 4)
done()