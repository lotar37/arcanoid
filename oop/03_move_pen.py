from math import sin, cos, radians
import tkinter
from time import sleep
from random import choice, randint

max_x = 480
max_y = 360

class Pen:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = "#" + hex(randint(8000000,16000000))[2:]
        self.step = 30

    def move(self, recurs=False):
        step = randint(5,self.step)
        angle = randint(0,359)
        _x = step * cos(radians(angle))
        _y = step * sin(radians(angle))
        canvas.create_line(self.x,self.y,self.x + _x, self.y + _y,fill=self.color,width=1)
        self.x = self.x + _x
        self.y = self.y + _y
        self.check_border()
        if recurs:
            canvas.after(20, self.move, True)

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
    for i in range(250):
        b.append(Pen(randint(0,max_x), randint(0,max_y)))
    for i in range(len(b)):
        canvas.after(25,b[i].move, True)

def init_main_window2():
    global root, canvas, scores_text, scores_value
    root = tkinter.Tk()
    root.title("PEN")
    canvas = tkinter.Canvas(root, width=max_x, height=max_y, bg="white")
    canvas.pack()
    b = []
    for i in range(50):
        b.append(Pen(randint(0,max_x), randint(0,max_y)))
    while True:
        for i in range(len(b)):
            b[i].move()
        # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться
        root.update_idletasks()
        # обновляем игровое поле и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано
        root.update()
        # canvas.update()
        sleep(0.001)
    # canvas.bind("<Button-1>",click_event_handler)

if __name__ == "__main__":
    init_main_window2()
    root.mainloop()
