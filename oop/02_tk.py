from math import sin, cos, radians, degrees
from time import sleep
import tkinter
from random import choice, randint

max_x = 480
max_y = 360


class Ball:
    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.step = 30
        self.Vx = self.step * cos(radians(self.angle))
        self.Vy = self.step * sin(radians(self.angle))
# движение шарика
    def move(self):
        self.x += self.Vx
        self.y += self.Vy
        print(self.x,"-",self.y)
        self.check_wall()
# изменение угла при достижении препятствия
# типы препятствий: top, right, bottom, left
    def change_angle(self,type):
        if type == "left":
            pass
# проверка наличия стены
    def check_wall(self):
        if self.x < 0:
            self.x = 0
            self.Vx = -self.Vx
        if self.x > max_x:
            self.x = max_x
            self.Vx = -self.Vx
        if self.y < 0:
            self.y = 0
            self.Vy = -self.Vy
        if self.y > max_y:
            self.y = max_y
            self.Vy = -self.Vy


b = Ball(5,5,30)
for i in range(30):
    b.move()
    sleep(0.1)






def init_main_window():
    global root, canvas, scores_text, scores_value
    root = tkinter.Tk()
    root.title("BALL")
    canvas = tkinter.Canvas(root, width=max_x, height=max_y, bg="white")
    # canvas.bind("<Button-1>",click_event_handler)
print(__name__)

if __name__ == "__main__":
    init_main_window()
    root.mainloop()