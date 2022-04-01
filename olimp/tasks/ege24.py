f = open("./data/24_demo.txt")
arr = f.readlines()
str = arr[0]
s = ""
c = 0
pred = ""
maximum = 0
i = 0
for simbol in str:
    i +=1
    # print(simbol)
    if pred != simbol:
    # if simbol == "X":
        c += 1
        pred = simbol
        s += simbol
    else:
        if c > maximum:
            maximum = c
        c = 0
            # print(s)
            # print(i)
        s = ""
print(maximum)

