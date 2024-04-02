n = 600000
a = []
while len(a)<5:
    aa = []
    for  i in range(8, int(n**0.5)+1):
        if n % i == 0 :
            if i % 10 == 7:
                aa.append(i)
                break
            elif n//i % 10 == 7:
                aa.append(n//i)
        if len(a):
            a.append([n, min(aa)])
    n += 1
    print(n,a)
print(a)