# from math import sqrt  as sss
# cnt = 0
# for i in range(45000000,50000001):
#     m = 0
#     a = []
#     for j in range(3,int(sss(i))+1, 2):
#         if i % j == 0:
#             m += 1
#             a.append(j)
#             # print(m,j)
#             if (i // j)%2 == 1:
#                 m += 1
#                 a.append(i // j)
#             if i // j == j:
#                 m -= 1
#                 # print(m, j)
#         if m > 5:
#             break
#
#
#     if m == 5:
#         cnt += 1
#         print(cnt , int(sss(i)), i, m, a)

#
# for i in range(185311,185330):
#     c = 0
#     a = [1,i]
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             c += 1
#             a.append(j)
#             a.append(i//j)
#         if c > 1:
#             break
#
#     if c == 1:
#
#         print(i, sorted(a))

# for i in range(400000000, 600000000):
#     n = i
#     c = 0
#     while n % 2 == 0:
#         n = n // 2
#         c += 1
#     if c % 2 == 1:
#         continue
#     c = 0
#     while n % 3 == 0:
#         n = n // 3
#         c += 1
#     if c % 2 == 0:
#         continue
#     if n == 1:
#         print(i)

for i in range(123456789, 223456790):
    a = []
    if int(i**0.5)**2 == i:
        for j in range(2, int(i**0.5) ):
            if i % j == 0:
                a.append(j)
                a.append(i//j)
            if len(a) > 2:
                break
    if len(a) == 2:
        print(i, max(a))
