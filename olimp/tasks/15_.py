k = 0
for A in range(300):
    for x in range(300):
        for y in range(300):
            if 2*x+3*y>30 or x + y <= A:
                k += 1
    if k == 90000:
        print(A)
        break