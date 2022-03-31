from random import randint
class player:
    name = ""
    def __init__(self,name):
        self.name = name

    def roll_the_dice(self):
        return randint(1,6)

class team:
    players = []
    name = ""
    def __init__(self, n, name):
        self.name =
        for i in range(n):
            self.players.append(player("name"+str(n)))

    def team_pass(self):
        summa = 0
        for pl in self.players:
            summa += pl.roll_the_dice()
        return summa

class game:
    teams = []
    def __init__(self, n):
        for i in range(n):
            self.teams.append(team())





