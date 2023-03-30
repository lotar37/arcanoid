# import random as r
#
# a = []
# for i in range(100000):
#     j = 0
#     for j in range(10):
#         if r.randint(1, 25) == 13:
#             a.append(1)
#             break
#
# print(len(a)/1000)
y = input("введите число \n")
print(y[0], y[1], y[2])
if y[0] == y[1] or y[1] == y[2] or y[0] == y[2]:
    print('yes')
else:
    print('no')
