class wolf:
    weight = 5
    lenght = 10
    name = ""
    food = 7
    point = 0
    status = "live"

    def __init__(self, w, n, p):
        self.weight = w
        self.name = n
        self.point = p

    def sleep(self):
        # print("zzzzzzz")
        pass

    def run(self):
        if self.weight > 0:
            self.weight -= 1
            self.eat()
            self.sleep()
        else:
            self.status = "die"
            print("волк", self.name, "прекратил игру (((")

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.weight +=1

    def info(self):
        return self.name + " | " + str(self.weight)+ " | " + str(self.point)

    def talk(self, question):
        if question == "Как тебя зовут?":
            print("Меня зовут ", self.name)
        elif question == "Вес?":
            print("Я вешу ", self.weight, " килограмм")
        elif question == "Где?":
            print("Я в точке ", self.point)
        else:
            print("Не понял вопрос")

    def life(self):
        if self.weight < 4:
            self.eat()
            self.sleep()



if __name__ == "__main__":
    vasja = wolf(30, "Вася")
    mosja = wolf(20, "Моисей")
    mosja.talk("Как тебя зовут?")