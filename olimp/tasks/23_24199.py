def foo(n):
    # print(n)
    if n % 6 == 0 or n < 1:
        return 0
    if n == 1:
        return 1
    s = foo(n-1)
    if not(n > 33 and n // 3 < 33):
        s += foo(n//3)
    if not (n > 33 and n // 4 < 33):
        s += foo(n//4)
    return s

print(foo(100))
print(6*8**4 + 7*8**3+5*8**2+4*8+3)