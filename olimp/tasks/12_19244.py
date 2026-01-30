a = {}
for i in range(3,10001):
    s = "1" + "2"*i
    print(s)
    while "12" in s or "322" in s or "222" in s:
        if "12" in s:
            s = s.replace("12","2",1)
        if "322" in s:
            s = s.replace("322","21",1)
        if "222" in s:
            s = s.replace("222","3",1)
    n = sum([int(ss) for ss in s])
    print(f"{s}={n}")
    if  n in a:
        a[n] += 1
    else:
        a[n] = 1

    if sum([int(ss) for ss in s]) == 40 or i == 200:
        a = sorted(a.items())
        print(i,a)
        break