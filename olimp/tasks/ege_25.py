# Рассмотрим произвольное натуральное число, представим его всеми возможными
# способами в виде произведения двух натуральных чисел и найдём для каждого
# такого произведения разность сомножителей. Например, для числа 16 получим:
# 16=16*1=8*2=4*4, множество разностей содержит числа 15, 6 и 0.
# Найдите все натуральные числа, принадлежащие отрезку [2000000;3000000],
# у которых составленное описанным способом множество разностей будет содержать
# не меньше трёх элементов, не превышающих 115.
# В ответе перечислите найденные числа в порядке возрастания.

# 2053440
# 2098080
# 2328480
# 2638944

import math

for i in range(2000001,3000000):
    arr = []
    count = 0
    for j in range(3,int(math.sqrt(i))+1):
        if i % j == 0:
            if abs(i//j - j) <= 115:
                count += 1
            if count > 2:
                print(i)
                break





