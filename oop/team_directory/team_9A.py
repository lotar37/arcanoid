# есть несколько команд(>=4)
#  в каждой команде несколько игроков(>=3)
# каждый игрок бросает игральную кость
# сумма выпавших чисел - ход команды
# если команда выкинула четную сумму - она выигрыла
# количество очков которые набирает равно количеству
# команд, выкинувших нечетную сумму

from random import randint

class Player:

    def __init__(self, name):
        self.name = name
        
    # бросить кость
    def roll_the_dice(self):
        a = randint(1,6)
        print("игрок команды",self.name,"бросил", a)
        return a


class Team:
    def __init__(self, n, team_name):
        self.team_name = team_name
        self.players = []
        # добавление игроков в команду
        for i in range(n):
            self.players.append(Player(self.team_name+":player"+str(i)))

    # ход команды(нахождение суммы выброшеных)
    def team_pass(self):
        summa = 0
        for pl in self.players:
            summa += pl.roll_the_dice()
        return summa

t = Team(8,"Harricane")
print(t.team_pass())

class Game:
    pass

# p = Player("bvz")
# print(p.roll_the_dice())