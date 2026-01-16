from importlib.metadata import pass_none
from random import randint

n = 7
a = [randint(1, 60) for _ in range(n)]
# print(sorted(a))
a = [a[i] - 1 if a[i] == a[i + 1] else a[i] for i in range(n - 1)] + [a[n - 1]]
# n = int(input())
# a = [int(s) for s in input().split()]
a = [6,3]
n = len(a)
a.sort()
a_distance = [a[i + 1] - a[i] for i in range(n - 1)]

# убрать нули

while 0 in a_distance:
    print(a_distance)
    i = a_distance.index(0)
    for j in range(i + 1, len(a)):
        a[j] += 1
    a_distance = [a[k + 1] - a[k] for k in range(n - 1)]

# print(a_distance)
a_distance = [0] + a_distance + [0, 0, 0, 0]
d = [[0, 0] for _ in range(n + 2)]
d[1][0] = a_distance[1]
for i in range(1, n):
    if d[i][0]:
        if d[i - 1][0] == 0:
            if d[i + 1][0] == 0:
                d[i + 1][0] = d[i][0] + a_distance[i + 1]
            else:
                if d[i + 1][0] > d[i][0] + a_distance[i + 1]:
                    d[i + 1][0] = d[i][0] + a_distance[i + 1]
        if d[i + 2][1] == 0:
            d[i + 2][1] = d[i][0] + a_distance[i + 2]
        else:
            if d[i + 2][1] > d[i][0] + a_distance[i + 2]:
                d[i + 2][1] = d[i][0] + a_distance[i + 2]

    if d[i][1]:
        if d[i + 1][0] == 0:
            d[i + 1][0] = d[i][1] + a_distance[i + 1]
        else:
            if d[i + 1][0] > d[i][1] + a_distance[i + 1]:
                d[i + 1][0] = d[i][1] + a_distance[i + 1]
        if d[i + 2][1] == 0:
            d[i + 2][1] = d[i][1] + a_distance[i + 2]
        else:
            if d[i + 2][1] > d[i][1] + a_distance[i + 2]:
                d[i + 2][1] = d[i][1] + a_distance[i + 2]

print(min(d[n - 1]))