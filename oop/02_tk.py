from math import sin, cos, radians, degrees
import tkinter
from random import choice, randint
from time import sleep

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
        self.step = 5
        self.dx = self.step * cos(radians(self.angle))
        self.dy = self.step * sin(radians(self.angle))
        self.avatar = Game.canvas.create_oval(self.x, self.y, \
            self.x + 2*self.radius, self.y + 2*self.radius, fill=self.color)
# движение шарика
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.check_wall()
        print(self.x, self.y)
        Game.canvas.coords(self.avatar, self.x, self.y, self.x + 2*self.radius, self.y + 2*self.radius)
        # Game.canvas.after(20,self.move)
# проверка наличия стены
    def check_wall(self):
        if self.x < 0:
            self.x = 0
            self.dx = -self.dx
        if self.x > max_x:
            self.x = max_x
            self.dx = -self.dx
        if self.y < 0:
            self.y = 0
            self.dy = -self.dy
        if self.y > max_y:
            self.y = max_y
            self.dy = -self.dy


class Game:
    scores_text = ""
    scores_value = ""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=max_x, height=max_y, bg="white")

    def __init__(self):
        Game.root.title("BALL")
        Game.canvas.pack()
        self.balls = []
        for i in range(10):
            self.balls.append(Ball(randint(0,max_x), randint(0,max_y), randint(0,359),choice(ball_available_colors)))
        for i in range(len(self.balls)):
            self.balls[i].move()
        # self.root.mainloop()

    def play(self):

        while True:
            sleep(0.05)
            print(1)
            for i in range(len(self.balls)):
                self.balls[i].move()
            self.root.update_idletasks()
            self.root.update()

print(__name__)

if __name__ == "__main__":
    g = Game()
    g.play()