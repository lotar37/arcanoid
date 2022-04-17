from math import sin, cos, radians, degrees, sqrt
import tkinter
from random import choice, randint
from time import sleep

max_x = 480
max_y = 360
ball_available_colors = ["green", "blue", "red", "yellow", "magenta", "black", "green",
                         "cyan", "pink", "orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange"]




class Ball:
    def __init__(self,x,y,angle,color,num):
        self.num = num
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.radius = 15
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
# проверка наличия стены
# если касается стенки - оттолкнуться
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

    def __init__(self, count):
        Game.root.title("BALL")
        Game.canvas.pack()
        self.balls = []
        for i in range(count):
            self.balls.append(Ball(randint(0,max_x), randint(0,max_y), randint(0,359),choice(ball_available_colors),i))
        for i in range(len(self.balls)):
            self.balls[i].move()

    def check_collision(self):
        for i in range(len(self.balls)-1):
            for j in range(i,len(self.balls)):
                delta = sqrt((self.balls[i].x - self.balls[j].x)**2 +  (self.balls[i].y - self.balls[j].y)**2 )
                if delta < (self.balls[i].radius + self.balls[j].radius)*1.5:
                    self.calculate_collision(i, j)

    def calculate_collision(self, i, j):
        if (self.balls[i].dx > 0 and self.balls[j].dx < 0) or \
                (self.balls[i].dx < 0 and self.balls[j].dx > 0):
            self.balls[i].dx = -self.balls[i].dx
            self.balls[j].dx = -self.balls[j].dx

        if (self.balls[i].dy > 0 and self.balls[j].dy < 0) or \
                (self.balls[i].dy < 0 and self.balls[j].dy > 0):
            self.balls[i].dy = -self.balls[i].dy
            self.balls[j].dy = -self.balls[j].dy
        self.balls[i].move()
        self.balls[j].move()

    def play(self):
        while True:
            sleep(0.05)
            self.check_collision()
            for i in range(len(self.balls)):
                self.balls[i].move()
            Game.root.update_idletasks()
            Game.root.update()

print(__name__)

if __name__ == "__main__":
    g = Game(3)
    g.play()