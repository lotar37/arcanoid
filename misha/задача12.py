s = '0' + '1' * 12 + '2' * 15 + '3' * 17
print(s)

while s.find('01') >= 0 or s.find('02') >= 0 or s.find('03') >= 0:
    if s.find('01') >= 0:
        s = s[:s.find('01')] + '20' + s[s.find('01')+2:]
    if s.find('02') >= 0:
        s = s[:s.find('02')] + '120' + s[s.find('02')+2:]
    if s.find('03') >= 0:
        s = s[:s.find('03')] + '302' + s[s.find('03')+2:]
    # input(s)
else:
    print(s.count('1'))

# Задание 1
# при помощи цикла for вывести на экран все числа в промежутке от 105 до 734 которые
# делятся без остатка на 3 и на 7
# - кратны 17 или 23
# - заканчиваются  на 3



# Задание 2
# список arr строится следующим образом:
import random
arr = []
for i in range(1000):
    arr.append(random.randint())

# найти, сколько четных чисел в списке arr
# определить является сумма элементов arr четным числом
# найти самое большое и самое маленькое число из списка