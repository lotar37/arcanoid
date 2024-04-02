from random import randint
n = 8
a = [randint(1, 30) for _ in range(n)]
n = int(input())
a = [int(s) for s in input().split()]
d = [1 for i in range(n)]

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] < a[j]:
            if d[i] >= d[j]:
                d[j] = d[i] + 1
print(max(d))