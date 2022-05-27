
# https://acmp.ru/index.asp?main=task&id_task=12
# Дачники


data = [
"6 6 3 6 6 9 8 7 5 4",
"13 5 9 2 9 8 12 8 12 2",
"3 2 2 1 2 3 6 3 6 1"
]
a = [[int(i) for i in s.split()] for s in data]
import math
# a = [[int(i) for i in input().split()] for s in range(int(input()))]

def qwarta(angle):
    if angle < 90:
        return "1"
    if angle < 180:
        return "2"
    if angle < 270:
        return "3"
    return "4"

def polar_transformation(a):
    # перемещаем  точку приземления в ноль
    for i in range(2,len(a),2):
        a[i] -= a[0]
    for i in range(3,len(a),2):
        a[i] -= a[1]
    polar = []
    for i in range(1,5):
        x = a[2*i]
        y = a[2*i + 1]
        if x == 0 and y == 0:
            return True
        angle = math.degrees(math.acos(x/math.sqrt(x*x + y*y)))

        if y < 0:
            angle = 360 - angle

        # print(x,y,angle)
        polar.append(angle)
    qwa = ""
    print(polar)
    for i in polar:
        if qwarta(i) not in qwa:
            qwa += qwarta(i)
    print(qwa)
    if len(qwa) < 3:
        return False
    else:
        return True
c = 0
for lst in a:
    if polar_transformation(lst):
        c += 1
print(c)
# print(polar_transformation(a[0]))
# print(polar_transformation(a[0]),polar_transformation(a[1]),polar_transformation(a[2]))

