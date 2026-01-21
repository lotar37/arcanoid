from random import randint
j = 4
n = 20*j
mx = 10*j
a_in = [randint(1,mx) for i in range(n)]

a = [0] * (mx + 1)
for i in a_in:
    a[i] += 1
# print(a)
# print(a_in)
for i in range(len(a)):
    if sum(a[i:]) >= i:
        level = i
    else:
        break

print(level)