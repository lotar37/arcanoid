s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(st,d):
    n = 0
    st = st[::-1]
    for i in range(len(st)):
        n += s.find(st[i])*d**i
    return n
print(convert("11111110",2))


for i in range(32,3009):
    if convert("KOT",i) + convert("GOLODNI",i) == convert("MEEOW",i)*convert("100",i) -20194023088:
        print(convert("PURR",i))
        break
