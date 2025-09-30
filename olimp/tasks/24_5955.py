s = open("./data/24_5955.txt").readline()

d = {"A": "0", "C": "1", "D": "1", "F": "1", "O": "0"}
def translate(p):
    res = ""
    ps = " --CADOF"
    for t in p:
        res += str(ps.index(t)% 2)

    if res == "1001":
        return False
    else:
        return True

m = 0
c = 0
for i in range(len(s)-5):
    if translate(s[i:i+4]):
        c += 1
    else:
        m = max(m,c+3)
        c = 0
print(m)
