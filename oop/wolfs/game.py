from wolf import wolf
from time import sleep
from random import randint

class game:
    wolfs = []
    def __init__(self, num):
        for i in range(num):
            self.wolfs.append(wolf(randint(12,15),"name"+str(i),randint(0,100)))

    def allInfo(self):
        for _wolf in self.wolfs:
            _wolf.talk("Как тебя зовут?")
            _wolf.talk("Вес?")
            _wolf.talk("Где?")


g  = game(3)
g.allInfo()




