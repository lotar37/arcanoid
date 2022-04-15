# Задание 17 № 37356

f = open("17.txt")
a = [int(i) for i in f]


count3 = 0
count34 = 0
# count1 = 0
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         count1 += 1
#         if a[i]*a[j]%34 != 0:
#             count34 += 1
#         if a[i] % 3 == 0 or a[j] % 3== 0:
#             count3 += 1
# print(count3, count1, count34)
#
#
#
# print(a[:20])
#

f = open("17.txt")
a = [int(i) for i in f]


maximum = 0
c = 0

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i]+a[j]) % 9 == 0:
            c += 1
            maximum = max(a[i]+a[j],maximum)
print(c, maximum)
















