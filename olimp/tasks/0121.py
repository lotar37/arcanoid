from random import randint
n = 10
a = [randint(1, 60) for _ in range(n)]
n = int(input())
a = [int(s) for s in input().split()]
a.sort()

d  =  [0 for i in range(n)]

d[1] = a[1]-a[0]
d[n-1] = a[n-1]-a[n-2]
for i in range(2, n-2):
    print(d)
    if d[i]:
        continue
    if a[i] - a[i-1] <= a[i+1] - a[i]:
        d[i] = a[i] - a[i-1]
    else:
        d[i+1] = a[i+1] - a[i]
    # if d[i] > 0 and d[i-1] > 0 and d[i-2] and i>2 > 0:
    #     d[i-1] = 0

print(sum(d))
print(a)
print(d)
