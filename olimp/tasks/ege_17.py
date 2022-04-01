# Задание 17 № 37356

f = open("17.txt")
arr = f.readlines()
print(arr[:20])

a = [int(string[:-1]) for string in arr]
a = []
for string in arr:
    a.append(int(string[:-1]))
m, count = 0, 0
print(len(a))
k = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        k += 1
        if (a[i] + a[j]) % 9 == 0:
            count += 1
            if (a[i] + a[j]) > m:
                m = (a[i] + a[j])
print(k, count, m)



