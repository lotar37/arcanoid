print(11000000**0.5)
n = 11000001
a = []
while len(a)<5:
    aa = []
    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            aa.append(n//m)
        if len(aa)==2:

            s = aa[0] + aa[1]
            # print(n, aa, len(a) )
            break
    if len(aa)==1:
        s = aa[0] + n//aa[0]
    print(n,s, aa)
    if 0 < s < 10000:
        a.append([n,s])

    n += 1
    s = 0
print(a)