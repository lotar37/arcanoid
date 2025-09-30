f = open('./data/17_2238.txt')
a = [int(i) for i in f]
av = sum(a) / len(a)
mx = c = 0
for i in range(2, len(a)):
    m = 0
    for j in range(i - 2, i+1):
        if a[j] > av:
            m += 1
        if m > 1:
            mx = max(mx, a[i-2] + a[i-1] + a[i])
            c += 1
print(c, mx)
