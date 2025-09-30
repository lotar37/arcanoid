import itertools as t

s = "АВИКПРЧЫ"
n = 1
aa = []
for a in t.product(s, repeat=5):
    s_a = ''.join(a)
    if n % 5 > 0:
        aa.append(1)
        for j in "ВКПРЧ":
            if j not in s_a:
                break
        else:
            print(a, n, len(aa))
            break
    n += 1
