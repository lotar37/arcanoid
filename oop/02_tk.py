from math import sin, cos, radians, degrees
import tkinter
from random import choice, randint

max_x = 480
max_y = 360
ball_available_colors = ["green", "blue", "red", "yellow", "magenta", "black", "green",
                         "cyan", "pink", "orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange"]


class Ball:
    def __init__(self,x,y,angle,color):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.radius = 5
        self.step = 30
        self.Vx = self.step * cos(radians(self.angle))
        self.Vy = self.step * sin(radians(self.angle))
        self.avatar = canvas.create_oval(self.x, self.y, \
            self.x + 2*self.radius, self.y + 2*self.radius, fill=self.color)
# движение шарика
    def move(self):
        self.x += self.Vx
        self.y += self.Vy
        self.check_wall()
        canvas.coords(self.avatar, self.x, self.y, self.x + 2*self.radius, self.y + 2*self.radius)
        canvas.after(200,self.move)
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



def init_main_window():
    global root, canvas, scores_text, scores_value
    root = tkinter.Tk()
    root.title("BALL")
    canvas = tkinter.Canvas(root, width=max_x, height=max_y, bg="white")
    canvas.pack()
    b = []
    for i in range(10):
        b.append(Ball(randint(0,max_x), randint(0,max_y), randint(0,359),choice(ball_available_colors)))
    for i in range(len(b)):
        canvas.after(20,b[i].move)
    # canvas.bind("<Button-1>",click_event_handler)
print(__name__)

if __name__ == "__main__":
    init_main_window()
    root.mainloop()