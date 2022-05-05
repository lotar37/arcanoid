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



# canvas.pack()
canvas = ""

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
        self.points = 0

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
            # sleep(0.01)
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
    def __init__(self, direct, x, y, color, id):
        self.player_id = id
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
                player = Game.players[int(Game.playing_field[self.y][self.x])]
                if player.id != self.player_id:
                    # нанесенный урон
                    damage = int(randint(50,100)/100 * self.power)
                    player.health -= damage
                    # начислить стрелявшему очки в размере ущерба
                    Game.players[self.player_id].points += damage
                    self.power = 0
                    print("игрок поймал маслину. Его здоровье", player.health)
                else:
                    print(self.id, "игрок стрелял сам в себя")
            else:
                self.power = int(0.75 * self.power)
        except:
            print("пуля вылетела за поле")



class Game(Frame):
    global move_types, root, canvas
    x = 17
    y = 17
    trees = 55
    players = []
    playing_field = []
    bullets = []
    mashtab = 40


    def __init__(self, n):
        global move_types, root, canvas
        root = Tk()
        super().__init__()
        max_x = 800
        max_y = 800
        self.tour = 0
        self.game_on = True
        self.alive = n
        self.proc = {"step":self.player_step, "shot":self.player_shot}
        self.lab = Label(canvas, bg='yellow', fg="black", text="в игре "+str(n))
        self.lab.grid(row=0, column=0)
        self.best = []
        self.best_control = n*2//3
        opts = {'ipadx': 5, 'ipady': 5, 'sticky': 'nswe'}
        for i in range(self.best_control):
            self.best.append(Label(canvas, bg='yellow', fg="black", text=" лучший из "+str(n)))
            self.best[len(self.best)-1].grid(row=i+1, column=1,**opts)
        canvas = Canvas(root, width=max_x, height=max_y, bg="black")
        canvas.grid(row=1, column=0,rowspan=self.best_control)

        Game.players = [Player(i) for i in range(n)]
        Game.playing_field = [["" for i in range(Game.y)] for j in range(Game.x)]
        self.arrangement()

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

    def change_score(self):
        self.lab["text"] = "в игре:" + str(self.alive)

    def check_player_health(self):
        for i in range(len(Game.players)):
            if Game.players[i].health <= 0 and Game.players[i].status != "die":
                Game.players[i].status = "die"
                canvas.delete(Game.players[i].avatar)
                canvas.delete(Game.players[i].health_ava)
                self.alive -= 1
                # self.change_score()




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
                    Game.players[move["id"]].color, move["id"]))

    def move_bullets(self):
        for bullet in Game.bullets:
            bullet.move()

    def best_players(self, n):
        points = []
        for player in Game.players:
            points.append(player.points)

        best = []
        for i in range(n):
            maximum = max(points)
            best.append([points.index(maximum), maximum, Game.players[points.index(maximum)].status, Game.players[points.index(maximum)].color])
            points[points.index(maximum)] = 0

        for i in range(len(best)):
            self.best[i]["text"] = "игрок {0} набрал {1}({2}) ".format(best[i][0], best[i][1], best[i][2])
            self.best[i]["bg"] = best[i][3]





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

    def take_winner(self):
        maximum = 0
        for player in Game.players:
            if player.status == "alive" and player.points > maximum:
                winner = player
                maximum = player.points
        return winner

    def play(self):
        while self.game_on:
            self.tour += 1
            if self.tour >= 500:
                break
            print("============ TOUR {} ================".format(self.tour))
            self.lab["text"] = "В игре {0}, тур {1}.".format(self.alive, self.tour)

            moves = self.players_move()
            # print(moves)
            self.game_calculate(moves)
            # print(Game.playing_field)
            self.best_players(self.best_control)
            root.update_idletasks()
            root.update()
            if self.alive <= 1:
                self.game_on = False
        winner = self.take_winner()
        print("Игра закончена. Cыграно {2} туров. Победил игрок№{0}, набравший {1} очков. Здоровье {3}."\
            .format(winner.id, winner.points, self.tour, winner.health))
        self.lab["text"] = "Игра закончена. Cыграно {2} туров. Победил игрок№{0}, набравший {1} очков. Здоровье {3}."\
            .format(winner.id, winner.points, self.tour, winner.health)
        sleep(5)
        root.mainloop()
            # sleep(1)


g = Game(30)
print(g.playing_field)

g.play()

