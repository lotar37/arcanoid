import random
win, lose = 0,0
while True:
    n = int(input('введи число: '))
    r = random.randint(1, 10)
    if (n + r) % 2 == 0:
        print('Комп выкинул', r, '. Cумма четная, ты выиграл')
        win  += 1
    else:
        print('Комп выкинул', r, '. Cумма нечетная, ты проиграл')
        lose += 1
    print('счёт === ' + str(win) + ':' + str(lose)+ ' ===')
