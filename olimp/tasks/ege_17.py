# Задание 17 № 37356

f = open("17.txt")
a = [int(i) for i in f]


count3 = 0
count34 = 0
count1 = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        count1 += 1
        if a[i]*a[j]%34 != 0:
            count34 += 1
        if a[i] % 3 == 0 or a[j] % 3== 0:
            count3 += 1
print(count3, count1, count34)



print(a[:20])


# m, count = 0, 0
# print(len(a))
# k = 0
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         k += 1
#         if (a[i] + a[j]) % 9 == 0:
#             count += 1
#             if (a[i] + a[j]) > m:
#                 m = (a[i] + a[j])
# print(k, count, m)



