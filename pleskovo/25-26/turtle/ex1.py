import turtle as joe
import random

joe.speed(0)
joe.bgcolor("black")
joe.color("yellow")
def starFill(length,n):
    joe.begin_fill()
    star(length,n)
    joe.end_fill()

def star(length,n):
    angle = n // 2 * 360 / n
    for i in range(n):
        joe.fd(length)
        joe.left(angle)


colors = ["yellow","red","cyan","magenta","blue","gray","green"]
a = [5,7,9,11,13,15,17]
for i in range(130):
    x = random.randint(-1000,1000)
    y = random.randint(-500,500)
    joe.color(random.choice(colors))
    joe.up()
    joe.setposition(x,y)
    joe.down()
    starFill(random.randint(20,60),random.choice(a))
