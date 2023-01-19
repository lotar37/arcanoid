# Известно, что у дракона может быть несколько голов и его сила определяется числом голов.
# Но как определить силу драконьей стаи, в которой несколько драконов и у каждого из них
# определенное число голов? Вероятно, вы считаете, что это значение вычисляется как сумма
# всех голов? Это далеко не так, иначе было бы слишком просто вычислить силу драконьей стаи.
# Оказывается, что искомое значение равно произведению значений числа голов каждого из драконов.
# Например, если в стае 3 дракона, у которых 3, 4 и 5 голов соответственно, то сила равна 3*4*5 = 60.
# Предположим, что нам известно суммарное количество голов драконьей стаи, как нам вычислить максимально возможное
# значение силы этого логова драконов? Именно эту задачу Вам и предстоит решить.

from math import sqrt
n  = int(input())
n = 6

i = int(sqrt(n))

m = n // i
print(i ** (m - 1)  * (n - (m - 1) * i))