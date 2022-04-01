x = int(input())
c = 0

for i in range(1,1500):
    if i*4>x:
        break
    for j in range(i,1500):
        if i + j*3 > x:
            break
        for k in range(j,1500):
            if x > i + j + 2 * k:
                c += x - i - j - 2*k
            else:
                break

print(c)


a = [1,2,3,4,5]
print(a[3])