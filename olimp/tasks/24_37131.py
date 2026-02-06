s = open("./data/24_37131.txt").readline()
m = 0
c = 1
for i in range(len(s)-1):
    if s[i]+s[i+1] in ["LK", "KL"]:
        m = max(c,m)
        c = 1
    else:
        c += 1
print(m)