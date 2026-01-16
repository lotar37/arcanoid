def foo(A, x, y):
    B = x < A
    C = y < A * 3
    D = 2 * x + y > 128
    return B and C or D

mn = 300
for a in range(300):
    c = 0
    for x in range(200):
        for y in range(200):
            if foo(a,x,y):
                c += 1
    if c == 40000:
        mn = min(mn, a)

print(mn)
