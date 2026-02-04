def foo(Amin, Amax,x):
    P = x >= 25 and x <= 64
    Q = x >= 40 and x <= 115
    A = x >= Amin and x <= Amax

    return P <= ((Q and (not A)) <= (not P))


minimum = 100
for mn in range(20,120):
    for mx in range(mn,121):
        if all([foo(mn,mx,xt) for xt in range(20,120)]):
            minimum = min(minimum, mx - mn)

print(minimum)
            
