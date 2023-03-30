#
# import numpy as np
# # a = 1
# # class Operations:
# #     def mod (self,a):
# #         if a >= 0:
# #             return a
# #         else:
# #             return -a
# #     def plus (self,a,b):
# #         return a+b
# # b = mod(a)
# # print(b)
# a = 'sdfsdf'
# print('d' in a)
# a = np.array([2443,5544])
# print(a)
#
# a, b, c = [1,2,4]
# print(b)


import random

# s = ''.join([str(random.randint(0,9)) for i in range(10)])

s = "8" * 120
while s.find('8888') >= 0 or s.find('222') >= 0:
    n = s.find('8888')
    if n >= 0:
        s = s[:n] + "22" + s[n+4:]
    n = s.find('222')
    if n >= 0:
        s = s[:n] + "88" + s[n+3:]


print(s)