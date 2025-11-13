s = "астек"

def convert(st, base):
    st = st[::-1]
    n=0
    for i in range(len(st)):
        n += s.find(st[i]) * base**i

    return n

print(convert("кектесак", 5) - convert("аттестат", 5))


def into(n,x1,x2):
    return n>=x1 and n<=x2

mn = 100
for y in range(99):
    for z in range(y,100):
        c = 0
        for x in range(100):
            if into(x,27,48) <= ((not into(x,39,60) and not into(x, y, z)) <= (not into(x,27,48) and into(x,30,55)) ):
                c += 1
        if mn == 100:
            mn = min(mn, z - y)

print(mn)