f = open("./data/24_demo.txt")
fl = f.readline()
print(len(fl))
pre = fl[0]
c = 0
maxim = 0
for i in range(1,len(fl)):
    if fl[i] != pre:
        c += 1
    else:
        if c > maxim:
            maxim = c
        c = 0
    pre = fl[i]
print(maxim)

