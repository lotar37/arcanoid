import itertools as t

s = "АВИКПРЧЫ"
n = 1
m = 0
for a in t.product(s, repeat=5):
    s_a = ''.join(a)
    print(a, set(a), len(set(a)), all([x not in "АИЫ" for x in a]), n)
    if n % 5 > 0:
        m += 1
        for j in "ВКПРЧ":
            if j not in s_a:
                break
        else:
            print(a, n, m)
            break
    n += 1
