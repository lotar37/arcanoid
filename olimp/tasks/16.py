# def F(n):
#     if n >= 19:
#         return F(n-4) + 3580
#     else:
#         return 6*(G(n-7)-36)
#
# def G(n):
#     if n>= 248045:
#         return n/20 + 28
#     else:
#         return G(n+9)-4


f = [0]*300000
g = [0]*300000
for n in range(300000):
    if n >= 19:
        f[n] = f[n-4]+3580
    else:
        f[n] = 6*(g[n-7] - 36)
    if n >= 248045:
        g[n] = n/20 + 28
    else:
        g[n] = g[n + 9] - 4
print(f[673])
# print(F(673))