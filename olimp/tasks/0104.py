# from random import randint
#
# a1 = [str(s) for s in range(4)]
# a2 = a1 + ["*", "?", "*", "?", "*", "?"]
# a1 += ["3", "4", "5", "6"]
# print(a1, a2)
# s = "".join([a1[randint(0, len(a1) - 1)] for ss in range(10)])
# mask = "".join([a2[randint(0, len(a2) - 1)] for ss in range(7)])
# print(s, mask)

#############################################3###3##
# ВСЁ ЧРЕЗМЕРНО УСЛОЖНИЛОСЬ. НУЖЕН ДРУГОЙ АЛГОРИТМ #
####################################################

# # # s, mask = "3123636546", "*1?0*??"
# s, mask = "0063326334",  "?0??*??"
# s, mask = "a", "?d"
# # s, mask = "ABBCDA", "A*CDA"
# # print(s, mask)
# j = many = one = 0
# # s = input()
# # mask = input()
#
# while mask.find("*?") > -1:
#     mask = mask.replace("*?", "?*")
# while mask.find("**") > -1:
#     mask = mask.replace("**", "*")
#
#
# def check(many, one, s, mask, no_sign=False):
#     if no_sign and s.count(mask) > 1:
#         s = s[s.rfind(mask):]
#     mask = mask.replace("*", "")
#
#     if one > len(s) or len(mask) > len(s):
#         print("NO")
#     elif many:
#         print("YES")
#     elif one == len(s):
#         print("YES")
#     else:
#         print("NO")
#
#
# while True:
#     print(many, one, s, mask)
#     if len(mask) == 0:
#         check(many, one, s, mask)
#         break
#     if mask.count("*")==0 and mask.count("?")==0:
#         check(many, one, s, mask,True)
#         break
#
#     if mask[0] == "*":
#         many = 1
#         mask = mask[1:]
#         continue
#     if mask[0] == "?":
#         one += 1
#         mask = mask[1:]
#         continue
#     if s[one:].find(mask[0]) > -1:
#         i = s[one:].find(mask[0])
#         if i == 0:
#             s = s[one + i + 1:]
#             mask = mask[1:]
#             many = 0
#             one = 0
#         elif i < 0:
#             print("NO")
#             break
#         elif many:
#             s = s[one + i + 1:]
#             mask = mask[1:]
#             many = 0
#             one = 0
#         else:
#             print("NO")
#             break
#     else:
#         check(many, one, s, mask)
#         break


