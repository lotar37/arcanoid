from math import sqrt
n = 59049
# n = 50

a = []
lim = int(sqrt(n)) +8
for i in range(3,lim ,2):
    limit = int(sqrt(i)) + 1
    for j in range(3, limit, 2):
        if i % j == 0:
            break
    else:
        a.append(i)

d = []

for i in range(len(a)):
    while n % a[i] == 0:
        d.append(a[i])
        n //= a[i]
    if a[i]>n:
        break
d.append(n)
print(a)
print(d, 3**10)
a5,a6,a7,a8,a9 = [],[],[], [],[]
for i in range(1,10000):
    if i * 3**9 <= 100000:
        a9.append(i * 3**9)
    elif i * 3**8 <= 100000:
        a8.append(i * 3**8)
    elif i * 3**7 <= 100000:
        a7.append(i * 3**7)
    elif i * 3**6 <= 100000:
        a6.append(i * 3**6)
    elif i * 3**5 <= 100000:
        a5.append(i * 3**5)

print(len(a9),len(a8),len(a7),len(a6),len(a5))
print(a9,a8,a7,a6,a5)