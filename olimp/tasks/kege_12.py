# from functools import reduce
# m = 0
# for i in range(210,301):
#     s = "3" + "7" * i
#     while "27" in s or "377" in s or  "777" in s:
#         if "27" in s:
#             s = s.replace("27", "32", 1)
#         if "377" in s:
#             s = s.replace("377", "27", 1)
#         if "777" in s:
#             s = s.replace("777", "3", 1)
#
#     n = reduce(lambda x,y:int(x)+int(y),s)
#     print(n)
#     if n % 15 == 0:
#         print(i,s)
#         m = i
# print(m)


from functools import reduce
m = 0
s = "9" * 96
while "22222" in s or "9999" in s:
    if "22222" in s:
        s = s.replace("22222", "99", 1)
    if "9999" in s:
        s = s.replace("9999", "2", 1)

print(s)

