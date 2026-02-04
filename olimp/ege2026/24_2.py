
s = open("./data/24_demo.txt").readline()
mx = 1
c = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        c += 1
    else:
        if c > mx:
            mx = c
        c = 1
print(mx)