a = [str(i) for i in range(10)]
a_ = [""] + a
print(a, a_)

for i in a:
    for j in a_:
        for k in a_:
            for m in a_:
                n = int("85"+i+"16"+j+k+m+"4")
                if n % 2658 == 0:
                    print(n, n // 2658)
