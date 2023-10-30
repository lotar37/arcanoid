# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки
# содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв N (если таких строк несколько, надо взять ту,
# которая находится в файле раньше), и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
f = open("./data/24_2.txt",'r')
minimum = 10000000
a = []
f = [i for i in f]
for s in f:
    if s.count("N") < minimum:
        print(minimum)
        minimum = s.count('N')
        a = [s[:-1]]
    elif s.count("N") ==  minimum:
        a.append(s[:-1])
alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = []
for i in range(len(alfa)):
    arr.append(a[0].count(alfa[i]))

print(arr)
m = 0
num = -1
for i in range(len(arr)):
    if arr[i] >= m:
        m = arr[i]
        num = i

print('буква:', alfa[num])



print(len(a))