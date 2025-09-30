def convert(n, k):
    a = ""
    while n > 0:
        a = str(n % k) + a
        n = n // k
    return a


# n = 2000
# d = 0
# while d != 57:
#     n += 1
#     d = int(convert(n)[::-1],2)
#
# print(n)

# for i in range(2,100):
#     n = convert(i,3)
#     if i % 2 == 0:
#         n = "" + n
from itertools import product

for i in product("123", repeat=2):
    print(i[0])

mn = 10000000000
for i in range(80, 10000):
    j = convert(i, 8)

    c = 0
    for k in j:
        if k in "0246":
            c += 1
    if c % 2 == 1:
        jj = j[-3:] + "46"
    else:
        jj = str(convert((i % 8) * 5, 8)) + j

    if int(jj, 8) == 38:
        print(i, j, jj, int(jj, 8))
    mn = min(mn, int(jj, 8))

print(mn)
