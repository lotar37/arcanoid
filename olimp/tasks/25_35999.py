from math import log2
print(int(log2(400000000/3)), 2**26*3)
a = []
for i in range(0 ,30):
    for j in range(1, 30):
        if 200000000 <= 2**i * 3**j <= 400000000 and i % 2 == 0 and j % 2 ==1:
            a.append(2**i * 3**j)
            print(i, j, 2**i * 3**j)
a.sort()
print(a)