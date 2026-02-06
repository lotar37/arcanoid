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










mn = 120
for a1 in range(1,120):
    for a2 in range(a1,120):
        flag = True
        for x in range(1,120):
            # f = foo(a1,a2,x)
            f = (25<=x<=64)<= (((40<=x<=115)and not(a1<=x<=a2))<=(not(25<=x<=64)))
            if f == False:
                flag = False
                break
        if flag == True:
            d = a2 - a1
            if d < mn:
                mn = d

print(mn)
        
                               
















            
