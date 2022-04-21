from tkinter import *
from random import randint, choice
from PIL import Image, ImageTk
from time import sleep
from threading import Thread
direct = ["n","o","s","w","n","o","s","w"]
move_types = ["shot","step"]
move_types_for_choice = ["shot"]+["step"]*4
ball_available_colors = ["green", "blue", "red", "yellow", "magenta",
                         "cyan", "pink", "orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange",
                         "green", "blue", "red", "yellow", "magenta",
                         "cyan", "pink", "orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange",
                         "green", "blue", "red", "yellow", "magenta",
                         "cyan", "pink", "orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange",
                         ]

max_x = 800
max_y = 800


root = Tk()
canvas = Canvas(root, width=max_x, height=max_y, bg="black")
canvas.pack()


class Player:
    global move_types, ball_available_colors, canvas, direct

    def __init__(self,id):
        self.id = id
        self.radius = 10
        self.color = ball_available_colors[self.id]
        self.status = "alive"
        self.hp = 100
        self.mashtab = 60
        self.x = 0
        self.y = 0
        self.health = 100

        # print(canvas)
        x,y,r = self.x,self.y,self.radius
        self.avatar = canvas.create_oval(x, y, x + 2*r, y + 2*r, fill=self.color)
        self.health_ava = canvas.create_rectangle(x + 2*r + 1, y,x + 2*r + 4, y+ 2*r,fill="green")

    def move(self):
        type = choice(move_types_for_choice)
        if type == "step":
            return {"id":self.id, "type":type,"data":self.step()}
        elif type == "shot":
            return {"id":self.id, "type":type,"data":self.shot()}

    def set_avatar(self):
        canvas.coords(self.avatar, self.x * Game.mashtab - self.radius, self.y * Game.mashtab - self.radius, \
                      self.x * Game.mashtab  + self.radius, self.y * Game.mashtab + self.radius)
        canvas.coords(self.health_ava,self.x * Game.mashtab  + self.radius + 1, \
                            self.y * Game.mashtab - self.radius, \
                            self.x * Game.mashtab + self.radius + 4, \
                            self.y * Game.mashtab + self.radius

                      )
    def move_avatar(self):
        pos = canvas.coords(self.avatar)
        discret = 10
        step = [-(pos[0] - self.x * Game.mashtab)//discret, -(pos[1] - self.y * Game.mashtab)//discret]
        # print("position:",pos,step)
        # print('to', self.x, self.y)
        for i in range(discret):
            if self.health >66:
                color = "green"
            elif self.health > 33:
                color = "yellow"
            else:
                color = "red"
            dec = 2*self.radius*(1-self.health/100)
            x, y = pos[0] + step[0] * (i+1) + Game.mashtab// 2,  pos[1] + step[1] * (i+1) + Game.mashtab// 2
            canvas.coords(self.avatar, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
            canvas.coords(self.health_ava, x + self.radius + 1, y - self.radius + dec, x + self.radius + 4, y + self.radius)
            canvas.itemconfig(self.health_ava, fill=color, outline=color)
            sleep(0.01)
            root.update_idletasks()
            root.update()

    def shot(self):
        d = choice(direct)
        if d == "n":
            return 0, -1
        if d == "o":
            return 1, 0
        if d == "s":
            return 0, 1
        if d == "w":
            return -1, 0

    def step(self):
        d = choice(direct)
        # print(self.id, d)
        if d == "n":
            if self.y == 0 or Game.playing_field[self.y-1][self.x] == "tree":
                return self.step()
            return 0, -1
        if d == "o":
            if self.x == Game.x - 1  or Game.playing_field[self.y][self.x + 1] == "tree":
                return self.step()
            return 1, 0
        if d == "s":
            if self.y == Game.y -1 or Game.playing_field[self.y + 1][self.x] == "tree":
                return self.step()
            return 0, 1
        if d == "w":
            if self.x == 0 or Game.playing_field[self.y][self.x-1] == "tree":
                return self.step()
            return -1, 0

    def step_exe(self, move):
        Game.playing_field[self.y][self.x] = ""
        self.x += move["data"][0]
        self.y += move["data"][1]
        Game.playing_field[self.y][self.x] = str(self.id)
        self.move_avatar()

class Bullet:
    def __init__(self, direct, x, y, color):
        self.power = 100
        self.direct = direct
        self.x = x
        self.y = y
        self.radius =  3
        self.color = color
        self.avatar = canvas.create_oval(self.x - self.radius, self.y - self.radius, \
            self.x + self.radius, self.y + self.radius, fill=self.color)

    def move_avatar(self):
        if self.x < 0 or self.x == Game.x or self.y < 0 or self.y == Game.y:
            self.power = 0
            canvas.delete(self.avatar)
        else:
            x = self.x * Game.mashtab + Game.mashtab // 2
            y = self.y * Game.mashtab + Game.mashtab // 2
            canvas.coords(self.avatar, x - self.radius, y - self.radius,\
                      x + self.radius, y + self.radius)

    def move(self):
        self.x += self.direct[0]
        self.y += self.direct[1]

        self.move_avatar()

        # проверка попадания
    def check_hit(self):
        try:
            print(self.x, self.y, Game.playing_field[self.y][self.x])
            if Game.playing_field[self.y][self.x] == "tree":
                self.power = 0
                print("пуля попала в дерево")
            elif Game.playing_field[self.y][self.x] != "":
                print("player", int(Game.playing_field[self.y][self.x]))
                player = Game.players[int(Game.playing_field[self.y][self.x])]
                print("до", player.health)
                player.health -= int(randint(50,100)/100 * self.power)
                print("после",player.health)
                self.power = 0
                print("игрок поймал маслину. Его здоровье", player.health)
            else:
                self.power = int(0.75 * self.power)
        except:
            print("пуля вылетела за поле")



class Game:
    global move_types, root, canvas
    x = 17
    y = 17
    trees = 55
    players = []
    playing_field = []
    bullets = []
    mashtab = 40

    def __init__(self, n):
        self.game_on = True
        Game.players = [Player(i) for i in range(n)]
        Game.playing_field = [["" for i in range(Game.y)] for j in range(Game.x)]
        self.arrangement()
        self.proc = {"step":self.player_step, "shot":self.player_shot}

    def move(self):
        pass
# начальная расстановка объектов и игроков
    def arrangement(self):
        for i in range(Game.trees):
            while True:
                x = randint(0, Game.x-1)
                y = randint(0, Game.y-1)
                if Game.playing_field[y][x] == "":
                    Game.playing_field[y][x] = "tree"
                    self.set_tree_img( x, y)
                    break
        for i in range(len(Game.players)):
            while True:
                x = randint(0, Game.x-1)
                y = randint(0, Game.y-1)
                if Game.playing_field[y][x] == "":
                    Game.playing_field[y][x] = str(i)
                    Game.players[i].x = x
                    Game.players[i].y = y
                    Game.players[i].set_avatar()
                    break

    # удаление дохлых пуль
    def check_bullets(self):
        # перебрать в обратном порядке, чтобы при удалении не было
        # ошибок индекса списка
        for i in range(len(Game.bullets)-1,-1,-1):
            Game.bullets[i].check_hit()
            if Game.bullets[i].power <= 0:
                canvas.delete(Game.bullets[i].avatar)
                Game.bullets.pop(i)

    def set_tree(self, x, y):
        delta = Game.mashtab // 2
        canvas.create_oval(x* Game.mashtab - delta, y* Game.mashtab - delta, x* Game.mashtab + delta,\
                           y* Game.mashtab + delta, fill="green")

    def set_tree_img(self, x, y):
        a_trees = ["../../images/tree5.gif","../../images/tree4.gif","../../images/tree6.gif","../../images/tree3.gif","../../images/tree2.gif"]
        minc = Image.open(choice(a_trees))
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(canvas, image=mincol, border=0)
        label3.image = mincol
        label3.place(x=x*Game.mashtab - 20 + Game.mashtab//2, y=y*Game.mashtab - 20 + Game.mashtab//2)

    def check_player_health(self):
        for i in range(len(Game.players)):
            if Game.players[i].health <= 0:
                Game.players[i].status = "die"
                canvas.delete(Game.players[i].avatar)
                canvas.delete(Game.players[i].health_ava)




    def players_move(self):
        moves = []
        self.check_player_health()
        for i in range(len(Game.players)):
            if Game.players[i].status != "die":
                moves.append(Game.players[i].move())
        return moves

    def player_step(self,move):
        Game.players[move["id"]].step_exe(move)

    def player_shot(self, move):
        Game.bullets.append(Bullet(move["data"],\
                    Game.players[move["id"]].x,\
                    Game.players[move["id"]].y,\
                    Game.players[move["id"]].color))

    def move_bullets(self):
        for bullet in Game.bullets:
            bullet.move()

    def game_calculate(self, moves):
        print(*[bul.power for bul in Game.bullets])
        # эта схема нужна для распределения ходов по приоритетам
        # сначала выполняются действия с наивысшим приоритетом,
        # потом следующие и так до самых низкоприоритетных
        for type in move_types:
            for i in range(len(moves)):
                if moves[i]["type"] == type:
                    self.proc[type](moves[i])
            if type == "shot":
                # двинуть пули
                self.move_bullets()
                # Проверка попаданий и на отсутствие энергии
                self.check_bullets()

    def play(self):
        i = 0
        while self.game_on:
            i += 1
            if i > 11150:
                break
            moves = self.players_move()
            print(moves)
            self.game_calculate(moves)
            print(Game.playing_field)
            root.update_idletasks()
            root.update()
            # sleep(1)


g = Game(25)
print(g.playing_field)
g.play()
