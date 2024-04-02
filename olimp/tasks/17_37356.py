a = [int(i) for i in open("./data/17.txt")]

maximum, count, c = 0, 0, 0
for i in range(len(a)-1):

    for j in range(i+1, len(a)):
        c += 1
        if (a[i] + a[j]) % 9 == 0:
            count += 1
            maximum = max(maximum, a[i] + a[j])
print(c, count, maximum)