import turtle as t
import time


def starFill(n, length):

    t.begin_fill()
    star(n, length)
    t.end_fill()


def star(n, length):
    t.speed(10)
    angle = n // 2 * 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

for i in range(5,16,2):
    starFill(i, 150)
    time.sleep(2)
    t.reset()