# def foo(n):
#     if n>20:
#         return 0
#     if n == 11:
#         return 0
#     if n == 20:
#         return 1
#     c = 0
#     c += foo(n+1)
#     c+= foo(n*2)
#     c += foo(n**2)
#     return c
# print(foo(2))
#
# print(int(bin(10)[2:]))
arr = []
import copy


def foo(n, a):
    if n < 6:
        return 0
    if n == 6 and 11 in a:
        arr.append(a)
        print(n, a, type(a))
        return 0
    if n > 6:
        b = c = copy.copy(a)
        if n - 1 >= 6:
            a.append(n - 1)
            foo(n - 1, a)
        if n - 2 >= 6:
            b.append(n - 2)
            foo(n - 2, b)
        if n // 3 >= 6:
            c.append(n - 2)
            foo(n // 3, c)


foo(16, [])
print(len(arr))
