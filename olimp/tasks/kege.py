# def to2(n):
#     c = ""
#     while n>0:
#         c = str(n%2) +c
#         n = n //2
#     c = (8 - len(c))*"0" + c
#     return c
#
# print(to2(16))
# m = 0
# for i in range(2,256):
#     n = to2(i)
#     m = max(m,int(n,2) - int(n[::-1],2))
# print(m)
from sys import exit
m = c = 0

for b1 in "епсух":
    for b2 in "епсух":
        for b3 in "епсух":
            for b4 in "епсух":
                for b5 in "псх":
                    if b1 + b2 + b3 + b4 + b5 == "успех":
                        m = c
                        print(b1 + b2 + b3 + b4 + b5, c +1)

                    c += 1
                    # if c > 100:
                    #     exit(123)

a = [[int(i)**2 for i in s.split()] for s in open("./data/9_2101.txt")]
c = 0
for arr in a:
    if max(arr) <= sum(arr) - max(arr):
        c += 1
print(c)

