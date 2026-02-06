import turtle as t
import colorsys as cs
t.speed(10)
n, a = 36, 30
circles = 120
for j in range(1,circles+1):
    
    t.color(cs.hsv_to_rgb(j/10,1,1))
    for i in range(n):
        t.fd(a)
        t.rt(360/n)

    t.rt(360/circles)
