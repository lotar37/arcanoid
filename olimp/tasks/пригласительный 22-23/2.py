# Нахождение наименьшего общего кратного

import math
d1 = 2*2*3*5
d2 = 2*3*7
# Разложение на простые множители
def decompose(n):
    a = []
    for i in range(2, int(math.sqrt(n))+2):
        while n % i == 0:
            a.append(i)
            n = n / i
        if n == 1:
            break
    return a

# Перемножение элементов списка
def prod(a):
    p = 1
    for n in a:
        p *= n
    return p

a1 = decompose(d1)
a2 = decompose(d2)
print(a1, a2)
# удаление повторяющихся элементов списков
for n in a1:
    if n in a1 and n in a2:
        a2.remove(n)
        a1.remove(n)
    # else:
    #     delta1.append(n)


nok = prod(a1) * d2
N = 2000
print(d1, d2, nok)
print(N//d1 + N//d2 - N//nok)
