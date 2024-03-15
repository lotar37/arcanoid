from math import ceil
N = int(input())
a = [int(i)  for i in input().split()]
K = int(input())

su = ceil(sum(a)/K)
min = su * 10
i = 0
while i < len(a):
    summa = 0
    for j in range(i,len(a)):
        summa += a[j]
        if summa >= su:
            if summa < min:
                min = summa
            i = j + 1
            break
    else:
        i = j + 1
print(min)
