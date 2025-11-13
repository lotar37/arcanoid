mn = 3005
print(False <= False)
m = 150
for X in range(m):
    for Y in range(X+1,m + 1):
        k = 0
        for t in range(m):
            if X >= 25 and X<=26 and Y <= 50:
                print(f"X:{X} Y:{Y} t:{t} (t>=25 and t<=64): {(t>=25 and t<=64)} (t >= X and t<= Y ): {(t >= X and t<= Y )} (t>=50 and t<=120): {t >= 50 and t <= 120} not:{not((t>=25 and t<=64) <= (t >= X and t<= Y ))}", not((t>=25 and t<=64) <= (t >= X and t<= Y )) <= (t>=50 and t<=120),k)
            if not((t>=25 and t<=64) <= (t >= X and t<= Y )) <= (t>=50 and t<=120):
                k+=1
        # if k:
        #     print(f"X:{X} Y:{Y} k:{k}")
        if k == 150:
            mn = min(mn,Y-X)

print(mn)