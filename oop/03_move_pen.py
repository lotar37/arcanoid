from math import sin, cos, radians
import tkinter
from random import choice, randint

max_x = 480
max_y = 360

class Pen:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = "#" + hex(randint(8000000,16000000))[2:]
        self.step = 30

    def move(self):
        step = randint(5,self.step)
        angle = randint(0,359)
        _x = step * cos(radians(angle))
        _y = step * sin(radians(angle))
        canvas.create_line(self.x,self.y,self.x + _x, self.y + _y,fill=self.color,width=5)
        self.x = self.x + _x
        self.y = self.y + _y
        self.check_border()
        canvas.after(20, self.move)

# проверяем выход за границы экрана и исправляем если вышли
    def check_border(self):
        if self.x > max_x:
            self.x = max_x
        if self.x < 0:
            self.x = 0
        if self.y > max_y:
            self.y = max_y
        if self.y < 0:
            self.y = 0


def init_main_window():
    global root, canvas, scores_text, scores_value
    root = tkinter.Tk()
    root.title("PEN")
    canvas = tkinter.Canvas(root, width=max_x, height=max_y, bg="white")
    canvas.pack()
    b = []
    for i in range(50):
        b.append(Pen(randint(0,max_x), randint(0,max_y)))
    for i in range(len(b)):
        canvas.after(25,b[i].move)
    # canvas.bind("<Button-1>",click_event_handler)

if __name__ == "__main__":
    init_main_window()
    root.mainloop()
