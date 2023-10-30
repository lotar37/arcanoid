f = open('data/17_7619.txt')
a = [int(i) for i in f]
print(a[:100])
maks = 0
for i in a:
    if len(str(i)) == 2:
        maks = max(i, maks)
print(maks)
count = 0
for i in range(len(a)-1):

    len_i, len_j = len(str(a[i])), len(str(a[i+1]))
    if (len_i == 2 or len_j == 2) and len_i != len_j:
        if ((a[i]+a[i+1]) % maks == 0):
            count += 1
            print(a[i],a[i+1], (a[i]+a[i+1]) % maks,count)