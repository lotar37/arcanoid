# pattern = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# def convert(n, sys):
#     num10 = 0
#     n = n[::-1]
#     for i in range(len(n)):
#         num10 += pattern.index(n[i])*sys**i
#     return num10
#
# start = pattern.index("H")
# print(start)
# for i in range(start+1,start+40000):
#     # if (convert("KOT",i) + convert("GOLODNI",i)) == (convert("MEEOW",i) * convert("100",i) - 20194023088):
#     if (convert("22A12E",i) + convert("2F1391",i) - convert("1H05D0",i)) % 19 == 0:
#         print((convert("22A12E",i) + convert("2F1391",i) - convert("1H05D0",i)) // 19)
#         break
#
# s = ["123","434","987"]
# print(*s)


# from random import randint
#
# n = randint(5,100)
# print(n)
# mx = 0
# for _ in range(n):
#     m = randint(1,30)
#     print(m, end=" ")
#     if m % 6 ==0 :
#         mx += m
# print("\n summa",mx)

# S = 'кинематограф'
# # S = 'пододеяльник'
# # S = 'чернокнижник'
# # S = 'удовольствие'
# # S = 'свистопляска'
# # S = 'единоборство'
# # S = 'небывальщина'
# # S = 'максимизация'
#
# print(S[5],end="-:-")
# print(S[4 : 8],end="-:-")
# print(S[: 8 : 2],end="-:-")
# print(S[: 6 : -1],end="-:-")
# print("\n second:")
# print(S[9], end="***")
# print(S[1:6], end="***")
# print(S[5::2], end="***")
# print(S[9:3:-1], end="***")
# n = 1350051
# a = []
#
# for x in range(1350051,n+100):
#     if len(a) == 5:
#         break
#     m = int(x*0.5)+1
#     l = m //100
#     if m % 100 < 11:
#         l -= 1
#     print(m,l)
#     for i in range(1,l):
#         # print(i*100 + 11)
#         if x % (i*100 + 11) == 0:
#             a.append([x,i*100 + 11])
#             break
# print(a)
#
# def simple_numbers(n):
#     a = [2]
#     for i in range(3,n+1):
#         for j in range(2,int(i**0.5)+1):
#             if i%j == 0:
#                 break
#         else:
#             a.append(i)
#     return a
# n = 1475000
# a_simple = simple_numbers(n//2)
# print(a_simple)
# result = []
# for i in range(n-1,n-1000,-1):
#     a = [0]
#     for j in a_simple:
#         if i % j == 0:
#             a += [j]
#     sm = sum(a)
#     if (0<sm<42000) and sm % 6 == 0:
#         result.append([i,sm])
#     if len(result) == 5:
#         break
# print(result)
#
#
#
#
#
#
#
# Дан список: a =  [10, 22, 9, 33, 21, 50, 41, 60, 80, 104,7]
# найти
# -количество нечетных чисел
# -сумму делящихся на три
# -среднее арифметическое двузначных
#
# from random import randint
# a = " ".join([f"{randint(4,120)}" for i in range(10)])
# print(f"s='{a}'")
# s = input("введите строку чисел: ")
#
# sm = 0
# a = [int(st) for st in s.split()]
# for n in a:
#     print("текущий n:",n)
#     input()
#     sm += n
#
# print(sm)
a = [
"Слух обо мне пройдет по всей Руси великой",
"Ветер кликать — зря голос срывать.",
"Ученье — свет, а неученье — тьма.",
"Кто рано встаёт, тому Бог подаёт.",
"Я к вам пишу — чего же боле? Что я могу еще сказать?",
"Учиться — одно, научиться — другое.",
"Полюбишь работу — и она тебя полюбит.",
"Семь раз отмерь — один раз отрежь.",
"Тише едешь — дальше будешь.",
"Старый друг лучше новых двух."]
print(" ".join([str(len(s)) for s in a]))
