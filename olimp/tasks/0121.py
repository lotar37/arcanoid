from random import randint
n = 10
a = [randint(1, 60) for _ in range(n)]
# n = int(input())
# a = [int(s) for s in input().split()]
a.sort()
a_distance = [a[i+1] - a[i] for i in range(n-1)]

# убрать нули

while 0 in a_distance:
    print(a_distance)
    i = a_distance.index(0)
    for j in range(i+1,len(a)):
        a[j] += 1
    a_distance = [a[k + 1] - a[k] for k in range(n - 1)]

print(a_distance)
d  =  [0 for i in range(n)]
for i in range(bet):
    
