from wolf import wolf
from time import sleep
from random import randint

class game:
    wolfs = []
    def __init__(self, num):
        for i in range(num):
            self.wolfs.append(wolf(randint(12,15),"name"+str(i),randint(0,100)))
        print(self.wolfs)

g  = game(3)
g.wolfs[0].talk("Как тебя зовут?")
g.wolfs[0].talk("Вес?")




