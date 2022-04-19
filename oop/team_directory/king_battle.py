from tkinter import *
from random import randint, choice
from time import sleep
from threading import Thread
direct = ["n","o","s","w","n","o","s","w"]
move_types = ["step"]
ball_available_colors = ["green", "blue", "red", "yellow", "magenta",
                         "cyan", "pink", "orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange"]

max_x = 800
max_y = 800


root = Tk()
canvas = Canvas(root, width=max_x, height=max_y, bg="black")
canvas.pack()


class Player:
    global move_types, ball_available_colors, canvas

    def __init__(self,id):
        self.id = id
        self.radius = 10
        self.color = ball_available_colors[self.id]
        self.status = "alive"
        self.hp = 100
        self.mashtab = 50
        self.x = 0
        self.y = 0
        print(canvas)
        self.avatar = canvas.create_oval(self.x, self.y, \
            self.x + 2*self.radius, self.y + 2*self.radius, fill=self.color)

    def move(self):
        type = choice(move_types)
        if type == "step":
            return {"id":self.id, "type":"step","data":self.step()}

    def set_avatar(self):
        canvas.coords(self.avatar, self.x * self.mashtab - self.radius, self.y * self.mashtab - self.radius, \
                      self.x * self.mashtab  + self.radius, self.y * self.mashtab + self.radius)



    def move_avatar(self):
        pos = canvas.coords(self.avatar)
        discret = 10
        step = [-(pos[0] - self.x * self.mashtab)//discret, -(pos[1] - self.y * self.mashtab)//discret]
        print("position:",pos,step)
        print('to', self.x, self.y)
        for i in range(discret):
            x, y = pos[0] + step[0] * (i+1),  pos[1] + step[1] * (i+1)
            canvas.coords(self.avatar, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
            sleep(0.001)
            root.update_idletasks()
            root.update()


    def step(self):
        global direct
        d = choice(direct)
        if d == "n":
            if self.y == 0 or Game.playing_field[self.y-1][self.x] != "":
                return self.step()
            return 0, -1
        if d == "o":
            if self.x == Game.x - 1  or Game.playing_field[self.y][self.x + 1] != "":
                return self.step()
            return 1, 0
        if d == "s":
            if self.y == Game.y -1 or Game.playing_field[self.y + 1][self.x] != "":
                return self.step()
            return 0, 1
        if d == "w":
            if self.x == 0 or Game.playing_field[self.y][self.x-1] != "":
                return self.step()
            return -1, 0

    def step_exe(self, move):
        Game.playing_field[self.y][self.x] = ""
        self.x += move["data"][0]
        self.y += move["data"][1]
        Game.playing_field[self.y][self.x] = str(self.id)
        self.move_avatar()


class Game:
    global move_types, root, canvas
    x = 15
    y = 15
    trees = 15
    playing_fild = []
    mashtab = 50

    def __init__(self, n):
        self.game_on = True
        self.players = [Player(i) for i in range(n)]
        Game.playing_field = [["" for i in range(Game.y)] for j in range(Game.x)]
        self.arrangement()
        self.proc = {"step":self.player_step}

# начальная расстановка объектов и игроков
    def arrangement(self):
        for i in range(Game.trees):
            while True:
                x = randint(0, Game.x-1)
                y = randint(0, Game.y-1)
                if Game.playing_field[y][x] == "":
                    Game.playing_field[y][x] = "tree"
                    self.set_tree( x, y)
                    break
        for i in range(len(self.players)):
            while True:
                x = randint(0, Game.x-1)
                y = randint(0, Game.y-1)
                if Game.playing_field[y][x] == "":
                    Game.playing_field[y][x] = str(i)
                    self.players[i].x = x
                    self.players[i].y = y
                    self.players[i].set_avatar()
                    break

    def set_tree(self, x, y):
        delta = Game.mashtab // 2
        canvas.create_oval(x* Game.mashtab - delta, y* Game.mashtab - delta, x* Game.mashtab + delta,\
                           y* Game.mashtab + delta, fill="green")

    def players_move(self):
        moves = []
        for i in range(len(self.players)):
            moves.append(self.players[i].move())
        return moves

    def player_step(self,move):
        self.players[move["id"]].step_exe(move)

    def game_calculate(self, moves):
        # эта схема нужна для распределения ходов по приоритетам
        # сначала выполняются действия с наивысшим приоритетом,
        # потом следующие и так до самых низкоприоритетных
        for type in move_types:
            for i in range(len(moves)):
                if moves[i]["type"] == type:
                    self.proc[type](moves[i])

    def play(self):
        i = 0
        while self.game_on:
            i += 1
            if i > 1115:
                break
            moves = self.players_move()
            print(moves)
            self.game_calculate(moves)
            print(Game.playing_field)
            root.update_idletasks()
            root.update()
            sleep(1)


g = Game(10)
print(g.playing_field)
g.play()
