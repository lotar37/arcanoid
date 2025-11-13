def F(n):
    G(n-50000) + G(n+50000)

def G(n):
    if n <= 6:
        return 5**n
    else:
        return G(n-3) + 2
s = 0
for i in range(50000,4,-3):
    if i <= 6:
        s += 5**i
    else:
        s+=2
for i in range(150000,4,-3):
    if i <= 6:
        s += 5**i
    else:
        s+=2

print(s)