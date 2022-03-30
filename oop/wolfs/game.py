from wolf import wolf
from time import sleep
from random import randint, choice

# список, из которого случайным образом выбирается количество еды, которая будет помещена
# в конкретной точке поля. Это конкретное состояние списка означает, что вероятность того,
# что в каждом поле еды не будет равна 4/7, будет единица еды - 2/7, две единицы еды - 1/7
arr = [0,0,0,0,1,1,2]

class game:
    wolfs = []
    game_on = True
    game_zone = []
    size_game_zone = 0
    # количество игроков, размер поля
    def __init__(self, num, size):
        self.size_game_zone = size
        for i in range(num):
            # задаём            вес                   имя           местоположение
            self.wolfs.append(wolf(randint(12,15), "name"+str(i), randint(0, size-1)))
        for i in range(size):
            # раскладываем еду по игровому полю. функция choice(arr) выбирает случайный элемент из списка arr
            self.game_zone.append(choice(arr))

    def allInfo(self):
        print("имя   |вес| точка")
        for wolf in self.wolfs:
            print(wolf.info())

    def wolf_eat_wolf(self,wolf_index1, wolf_index2):
        #pass означает, что функция определена, но ничего не делает
        pass

    def check_lives_wolfs(self):
        arr = []
        for wolf in self.wolfs:
            if wolf.status != "die":
                arr.append(wolf.name)
        return arr

    def wolfs_step(self):
        # проверяем количество живых волков
        # если оно равно 1 - у нас есть победитель
        # если 0 - игра тоже закончилась, но победителя нет
        # если > 1 - игра продолжается
        wolf_lives = self.check_lives_wolfs()
        if len(wolf_lives) == 1:
            self.game_on = False
            print("Игра окончена. Победил волк ",wolf_lives[0])

        elif len(wolf_lives) == 0:
            self.game_on = False
            print("Игра окончена. Никто не победил.")
        else:
            # для всех волков
            for wolf in self.wolfs:
                # если волк die, переходим к следующему
                if wolf.status == "die":
                    continue
                # перемещаем волка в случайную точку карты
                wolf.point = randint(0,self.size_game_zone-1)
                # если в точке есть еда - съедаем
                if self.game_zone[wolf.point] > 0:
                    print(wolf.name,"cъел", self.game_zone[wolf.point], "кг")
                    wolf.food += self.game_zone[wolf.point]
                    self.game_zone[wolf.point] = 0
                # побегать по местности, поесть(если есть еда), поспать
                wolf.run()

    def main(self):
        num = 0
        # главный игровой цикл
        while self.game_on:
            num += 1
            print("================ тур №", num, "====================")
            # игроки делают ход. расчет состояний.
            # выдача информации о текущем состоянии
            self.allInfo()
            # проверка: не оказались ли два волка в одной точке.
            # если оказались, то один отберет еду у другого, а если еды нет,
            # то он его съест (вот такая она, зверская жизнь...)
            for i in range(len(self.wolfs)-1):
                for j in range(i+1, len(self.wolfs)):
                    if self.wolfs[i].point == self.wolfs[j].point:
                        self.wolf_eat_wolf(i, j)
            # задержка перед следующим шагом
            sleep(0.1)
            self.wolfs_step()

# определяем игру с 10 игроками и 100 точками расположения
g  = game(10,100)
g.main()