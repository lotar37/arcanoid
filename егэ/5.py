def foo(n, s):
    st = ""
    while n  > 0:
        st = str(n%s) + st
        n //= s
    return st

def uff(st,s):
    st = st[::-1]
    n = 0
    for i in range(len(st)):
        n += int(st[i])*s**i
    return n

for i in range(150, 192):
    n = 2
    print(i, foo(i,n), uff(foo(i,n),n))

DЯ = 12