import turtle as t
import time, random


def starFill(n, length):
    t.color("yellow")
    t.begin_fill()
    star(n, length)
    t.end_fill()


def star(n, length):
    t.speed(12)
    angle = n // 2 * 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

window = t.Screen()
window.bgcolor("black")
window.setup(700,500)
a = [5,7,9,11,13,15]
for i in range(90):

    t.up()
    x = random.randint(-320,320)
    y = random.randint(-220,220)
    t.setposition(x,y)
    t.down()
    starFill(random.choice(a), random.randint(10,20))
t.up()
t.setposition(1000,y)
t.done()
