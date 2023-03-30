# Обозначим остаток от деления натурального числа a на натуральное число b как a mod b.
# Алгоритм вычисления значения функции F(n), где n— целое неотрицательное число, задан следующими соотношениями:
# F(0) = 0;
# F(n) = F(n − 1) + 1, если n > 0 и при этом n mod 3 = 2;
# F(n) = F((n − n mod 3) / 3), если n > 0 и при этом n mod 3 < 2.
# Укажите наименьшее возможное n, для которого F(n)=5.

def fun(n):
    if n == 0:
        return 0
    elif n % 3 == 2:
        return fun(n - 1) + 1
    else:
        return fun((n - n % 3) / 3)

def foo2(n):
    if n>3:
        return foo2(n-3)*n
    else:
        return n

p = 242
while p > 0:
    s = fun(p)
    print(p, s)
    if s == 5:
        break
    p -= 1


print(foo2(11))