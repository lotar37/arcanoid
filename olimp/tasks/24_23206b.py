s = open("./data/24_23206.txt").readline()
c = 0
for ct in '2468':
    s = s.replace(ct,'0')
for st in s.split('0'):
    if st.count('S') < 35:
        continue
    if st.count('S') == 35:
        c = max(c, len(st) + 1)
    else:
        for i in range(len(st)):
            if st[:i].count('S') == 36:
                c = max(c, i)
                break
print(c)