# def f(n):
#     if int(n**0.5)**2 == n:
#         return n**0.5
#     else:
#         return f(n+1) +1
#
# def f2(n):
#     if n<2025:
#         return n+3+f2(n+3)
#     else:
#         return n
#
# print("now:",f2(2018) - f2(2022))
#
# print(f(4850) + f(5000))

def foo(n):
    if n <= 15:
        return n*n + 11
    else:
        if n % 2:
            return foo(n-1) + 2 * n + 3
        else:
            return foo(n//2) + n**3 - 5*n


c = 0
for i in range(1,1001):
    if (str(foo(i))).count("6") > 2:
        c += 1



print(c)
