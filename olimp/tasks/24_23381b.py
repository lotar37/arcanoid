s = open("./data/24_23381.txt").readline()

c = 0


for ct in '2468':
    s = s.replace(ct,'0')

for st in s.split('0'):
    for i in range(len(st) - 1):
        if st[i] != st[i + 1]:
            break
    else:
        c = max(c,len(st))
print(c + 2)