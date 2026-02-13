s = open("./data/24_23381.txt").readline()

def getNum(s):
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            return 0
    else:
        return len(s)

for st in "2468":
    s = s.replace(st,"0")
m = 0
for st in s.split("0"):
    m = max(m,getNum(st))

print(m+2)