max = [0,0]
for i in range(193,1300):
    s = "1" * i
    while s.find("1111")>-1:
        s = s[:s.find("1111")]+"22" + s[s.find("1111") + 4:]
        if s.find('222')>-1:
            s = s[:s.find("222")] + "1" + s[s.find("222") + 3:]

    if s.count("1") > max[0]:
        max = [s.count("1"), i]
    print(s,i,max)

print(max)