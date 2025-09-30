a= [int(n) for n in open("./data/17_2401.txt")]
mn = c = 0
for i in range(len(a)-1):
        if 50 <= abs(a[i]) + abs(a[i+1]) <= 200:
            c += 1
            mn = min(mn, min(a[i],a[i+1]))
print(mn,c)