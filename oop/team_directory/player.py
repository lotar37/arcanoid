from random import randint

class Player:

    def __init__(self, name):
        self.player_name = name

    # бросить кости
    def roll_the_dice(self):
        a = randint(1,6)
        # print("игрок", self.player_name, "бросил кость на ", a)
        return a


class Team:
    # параметры:количество игроков, название команды
    def __init__(self, n, team_name):
        # количество набранных командой очков
        self.points = 0
        # список(хранилище) игроков команды
        self.players = []
        # имя команды
        self.team_name = team_name
        # Наполнение списка игроков.
        # В список помещаются относящиеся к команде игроки.
        for i in range(1, n+1):
            self.players.append(Player(self.team_name + ":player_"+str(i)))
    # ход команды = сумма ходов игроков
    def team_pass(self):
        summa = 0
        for pl in self.players:
            summa += pl.roll_the_dice()
        return summa
    # вывод на экран состава команды
    def team_list(self):
        print("состав команды", self.team_name)
        for pl in self.players:
            print(pl.player_name)




class Game:
    # сумма, которой будет достаточно для победы
    game_limit = 101
    # переменная game_on равна True если игра продолжается, и
    # False если выполнено условие окончания игры(какая-то из команд выигрыла)
    game_on = True
    # тип игры
    type = "четность"

    # n команд по  k игроков
    def __init__(self, n, k, type="четность"):
        self.teams = []
        self.type = type
        for i in range(1, n+1):
            self.teams.append(Team(k, "team_"+str(i)))

    # проверка, не набрала ли одна из команд достаточное для победы количество очков
    def check_points(self):
        for t in self.teams:
            if t.points >= self.game_limit:
                self.game_on = False
                print("Игра закончена. Победила команда ", t.team_name)
                return 0

    # вывод на экран текущего количество очков, набранных командами
    def view_points(self):
        print("oчки", end=":")
        for t in self.teams:
            print(t.points, end=", ")
        print("")

    # вывод на экран составов всех команд
    def team_lists(self):
        for t in self.teams:
            t.team_list()



    # в этом методе класса game команды набирают очки
    # Со всех команд собираются числа через метод team_pass класса team
    # те у кого числа четные имеют выигрышный билет и получают столько очков, сколько
    # команд с нечетными суммами. Если играют 4 команды и 2 выкинули четные, а
    # две нечетные суммы, то первые получают по два очка.
    def play(self):
        tour = 0
        # главный игровой цикл:
        # цикл, продолжающийся, пока не выполнится условие окончания игры
        while self.game_on:
            tour += 1
            print("---===== ТУР №" + str(tour) + " =======---")
            # a_team_pass - пустой список, для сбора с команд информаци о новом ходе
            a_team_pass = []
            # заполнение списка a_team_pass
            for t in self.teams:
                a_team_pass.append(t.team_pass())
            # выводим список с ходами команд
            print("ход команд:",a_team_pass)
            # анализируем ходы команд на четность:
            # если число четное вместо него пишем 1
            # если нечетное - 0
            for i in range(len(a_team_pass)):
                if a_team_pass[i] % 2 == 0:
                    a_team_pass[i] = 1
                else:
                    a_team_pass[i] = 0
            # количество очков, которые получат победившие команды
            # равно количеству проигравших команд. Чем меньше выигравших
            # команд, тем большее количество очков они получат.
            # len - метод возвращающий длину списка  sum - суммирует единицы в списке
            bonus = len(self.teams) - sum(a_team_pass)
            for i in range(len(a_team_pass)):
                if a_team_pass[i] == 1:
                    self.teams[i].points += bonus
                    print("команда", self.teams[i].team_name, "получает", bonus)
            # вывести очки, набранные командами
            self.view_points()
            # проверить, не набрала ли какая-либо команда достаточное
            # для победы количество очков, и если набрала - закончить игру
            self.check_points()

# создаём игру для шести команд по восемь игроков
g = Game(6, 8)
# выдать списки игроков команд
print("-СОСТАВЫ КОМАНД-")
g.team_lists()
g.play()








