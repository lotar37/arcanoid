n = input()
a = [int(s) for s in input().split()]
next = False
s = 0
for i in range(len(a) - 2):
    if next:
        next = False
        continue
    if abs(a[i] - a[i+1]) + abs(a[i+2] - a[i+1]) < abs(a[i] - a[i+2]) * 3:
        s += abs(a[i] - a[i+1])
        if i == len(a)-3:
            s += abs(a[i+2] - a[i + 1])

    else:
        s += abs(a[i] - a[i+2]) * 3
        next = True
print(s)