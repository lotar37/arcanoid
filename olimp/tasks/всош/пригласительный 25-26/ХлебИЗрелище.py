from random import randint
from datetime import datetime
start = datetime.now()
n = 18
t = 4
mn = 1000000
a_in = [randint(1,14) for i in range(n)]
for i in range(n-2*t-1):
    for j in range(i+t+1, n-t):
        if sum(a_in[i:i+t]) + sum(a_in[j:j+t]) < mn:
            mn = sum(a_in[i:i+t]) + sum(a_in[j:j+t])
            # print(i,j)

print(mn)
# print(a_in)
print(datetime.now() - start)
start = datetime.now()
#
# для ускорения работы алгоритма создаем вспомогательный список,
# состоящий из сумм отрезков длины t, который можно будет обработать
# в один проход продвигаясь по индексу и выбирая минимальную непересекающуюся сумму
# сопоставляя ее с текущим минимумом

a_sum = [sum(a_in[i:i+t]) for i in range(n-t)]


for i in range(len(a_sum)-t-1):
    if a_sum[i] + min(a_sum[i+t+1:])<mn:
        mn  = a_sum[i] + min(a_sum[i+t+1:])
print(mn)
print(datetime.now() - start)