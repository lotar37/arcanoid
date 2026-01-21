# def worm(index,energy):
#     print(index,energy)
#     if index>=len(a):
#         print(f"index>=len(a) index,energy=({index},{energy})")
#         return 0
#     if energy - a[index] < 0:
#         print(f"energy - a[index] < 0 ({energy} - {a[index]} )")
#         return 0
#     elif index == len(a)-1:
#         return energy - a[index]
#     aa = [-1]
#     for i in range(1, energy + 1):
#         e = worm(index + i, energy - i)
#         print(index + i,e,aa)
#         if e>0:
#             aa.append(e)
#
#     # print(aa)
#     return max(aa)
#
# from random import randint
# E = 6
# a = [randint(-10, 20) if i% 7==0 else randint(-2, 5)   for i in range(5)]
# print(a)
# print(a,worm(0, E))

import sys
from random import randint
print(5*6**6 + 4*6**5 + 4*6**4 + 3*6**3 + 2*6**2 + 6 + 2)
sys.exit(0)

# e = int(input())
# n = int(input())
n = 10
e = 3
a = [0]+[randint(-10, 15) if i % 7 == 0 else randint(-2, 5) for i in range(n)] + [0]

# a = [0] + [int(input()) for i in range(n)] + [0]
f = [e] + [0] * (n + 1)
print("a",a)
print("======= список f =======")
print(0,f)
for i in range(1, n + 2):
    m = -1
    for j in range(0,i):
        m = max(m, f[j]-(i-j))
    if m < 0:


        print(-1)
        sys.exit(0)
    f[i] = m + a[i]
    print(i,f)

for i in range(1):
    pass