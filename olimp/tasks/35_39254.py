from functools import reduce

N = 500000001
a = []
while len(a) < 5:
    aa = []
    if (int(N ** 0.5)) ** 2 == N:
        aa.append(N ** 0.5)
    for i in range(2, int(N ** 0.5)):
        if N % i == 0:
            aa.extend([i, N // i])
    if len(aa) > 4:
        aa.sort()
        # обработка последовательности в одно значение
        P = reduce(lambda a, b: a * b, aa[:5], 1)
        if P < N:
            a.append([P, N])

    N += 1
print(a)
