def fu(n):
    if n > 16:
        return 0
    if n == 16:
        return 1
    return fu(n + 1) + fu(n * 2) + fu(n ** 2)

def fu2(n):
    if n > 65:
        return 0
    if n == 65:
        return 1

    return fu2(n+1) + fu2(n*2) + fu2(n**2)

print( fu(2) * fu2(32))