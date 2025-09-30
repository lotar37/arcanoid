# # https://acmp.ru/index.asp?main=task&id_task=12
# # Дачники
#
#
# data = [
#     "6 6 3 6 6 9 8 7 5 4",
#     "4 0 -1 0 -1 5 5 5 5 0",
#     "13 5 9 2 9 8 12 8 12 2",
#     "3 2 2 1 2 3 6 3 6 1"
# ]
# a = [[int(i) for i in s.split()] for s in data]
# import math
#
#
# # a = [[int(i) for i in input().split()] for s in range(int(input()))]
#
#
# def turn_rectanle(rect):
#     m = 360 - max(rect)
#     return [(int(angle + m)) % 360 for angle in rect]
#
#
# def polar_transformation(a):
#     # перемещаем  точку приземления в ноль
#     for i in range(2, len(a), 2):
#         a[i] -= a[0]
#     for i in range(3, len(a), 2):
#         a[i] -= a[1]
#     polar = []
#     for i in range(1, 5):
#         x = a[2 * i]
#         y = a[2 * i + 1]
#         if x == 0 and y == 0:
#             return True
#         angle = math.degrees(math.acos(x / math.sqrt(x * x + y * y)))
#
#         if y < 0:
#             angle = 360 - angle
#
#         # print(x,y,angle)
#         polar.append(angle)
#     qwa = ""
#
#     polar = turn_rectanle(polar)
#     polar.append(360 - polar[0])
#     print(polar)
#     for i in range(4):
#         if abs(polar[i] - polar[i + 1]) > 180:
#             return False
#     return True
#
#
# c = 0
# for lst in a:
#     if polar_transformation(lst):
#         c += 1
# print(c)
# # print(polar_transformation(a[0]))
# print(polar_transformation(a[0]),polar_transformation(a[1]),polar_transformation(a[2]))

# Второе решение - преобразование координат
import math
from sys import exit

n = int(input())
b = [[int(i) for i in input().split()] for _ in range(n)]
# b = [[int(i) for i in s.split()] for s in data]

# print(a)

print(b)


def normalize(a):
    return [(a[i] - a[2]) if i % 2 == 0 else (a[i] - a[3]) for i in range(0, len(a))]

arr = []
c = 0

for j in range(len(b)):
    for i in range(2,len(b[j])-2,2):
        if b[j][0] != b[j][i] or b[j][1] != b[j][i+1]:
            arr.append(b[j])
        else:
            c += 1

b = arr
dd = []
for i in range(len(b)):
    dd.append(normalize(b[i]))

for d in dd:
    X = ((d[2] - d[8]) ** 2 + (d[3] - d[9]) ** 2) ** 0.5
    Y = ((d[2] - d[4]) ** 2 + (d[3] - d[5]) ** 2) ** 0.5
    if d[5] != 0:
        angle = math.atan(d[4] / d[5])
    else:
        angle = 0
    x0 = d[0] * math.cos(angle) - d[1] * math.sin(angle)
    y0 = d[0] * math.sin(angle) + d[1] * math.cos(angle)
    if 0 <= x0 <= X and 0 <= y0 <= Y:
        c += 1
    else:
        res = False
print(c)
