from random import randint
class Player:

    def __init__(self, name):
        self.player_name = name

    def roll_the_dice(self):
        a = randint(1,6)
        print("игрок", self.player_name, "бросил кость на ", a)
        return a


class Team:
    # players = []
    # параметры:количество игроков, название команды
    def __init__(self, n, team_name):
        self.team_name = ""
        self.points = 0
        self.players = []
        print("Создание команды", team_name, n)
        self.team_name = team_name
        for i in range(1, n+1):
            print(self.team_name + ":player_"+str(i))
            self.players.append(Player(self.team_name + ":player_"+str(i)))

    def team_pass(self):
        summa = 0
        for pl in self.players:
            summa += pl.roll_the_dice()
        return summa

    def sostav(self):
        print("состав команды", self.team_name)
        for pl in self.players:
            print(pl.player_name)




class Game:

    game_limit = 101
    game_on = True

    # n команд по  k игроков
    def __init__(self, n, k):
        self.teams = []
        for i in range(1, n+1):
            self.teams.append(Team(k, "team_"+str(i)))

    def check_points(self):
        for t in self.teams:
            if t.points >= self.game_limit:
                self.game_on = False
                print("Игра закончена. Победила команда ", t.team_name)
                return 0

    def view_points(self):
        print("oчки", end=":")
        for t in self.teams:
            print(t.points, end=", ")

    def sostavs(self):
        for t in self.teams:
            t.sostav()



    # в этом методе класса game команды набирают очки
    # Со всех команд собираются числа через метод team_pass класса team
    # те у кого числа четные имеют выигрышный билет и получают столько очков, сколько
    # команд с нечетными суммами. Если играют 4 команды и 2 выкинули четные, а
    # две нечетные суммы, то первые получают по два очка.
    # надпись pass означает, что метод этот ещё не написан и его следует написать
    def play(self):
        while self.game_on:
            a = []
            for t in self.teams:
                a.append(t.team_pass())
            print(a)
            for i in range(len(a)):
                if a[i] % 2 == 0:
                    a[i] = 1
                else:
                    a[i] = 0
            bonus = len(self.teams) - sum(a)
            for i in range(len(a)):
                if a[i] == 1:
                    self.teams[i].points += bonus
                    print("команда", self.teams[i].team_name, "получает", bonus)
            self.view_points()
            self.check_points()


g = Game(4, 3)
g.sostavs()
g.play()








