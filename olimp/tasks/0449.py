d = int(input().split()[0])
a = sorted([int(i) for i in input().split()])
b = a[0]
c = 1
for n in a:
    if n > b + d*2:
        c += 1
        b = n
print(c)