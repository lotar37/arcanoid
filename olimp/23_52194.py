# Исполнитель преобразует число на экране.
# У исполнителя есть две команды, которым присвоены номера.
# 1.Прибавить 1.
# 2.Умножить на 2.
#
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
# Программа для исполнителя это последовательность команд. Например, если в
# начальный момент на экране находится число 1, то программа 212 последовательно
# преобразует его в 2, 3, 6.
#
# Сколько существует программ, которые преобразуют исходное число 1 в число 16
# и при этом никакая команда не повторяется более двух раз подряд?
from datetime import datetime


def foo(start, stop, comand=""):
    if start > stop or comand[-3:] == "+++" or comand[-3:] == "***":
         return 0
    elif start == stop:
        return 1
    else:
        return foo(start + 1, stop, comand + "+") + foo(start * 2, stop, comand + "*")

start = 1
stop = 25000
time = datetime.now()
print(foo(start,stop))
print(datetime.now() - time)

time1 = datetime.now()
a = [[] for i in range(stop+1)]
a[1].append("")

add = [[0]*3 for _ in range(stop*2)]
mul = [[0]*3 for _ in range(stop*2)]

add[2][1]=1
mul[2][1]=1

for i in range(2,stop):
    if add[i][1]:
        


print(len(a[-1]))
print(datetime.now() - time1)