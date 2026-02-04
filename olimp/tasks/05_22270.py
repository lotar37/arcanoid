def convert(n, m):
    lit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = ""
    while n>0:
        s += lit[n%m]
        n //= m

    return s[::-1]

for i in range(430,600):
    print(convert(i,16))

