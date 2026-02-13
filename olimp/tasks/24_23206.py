s = open("./data/24_23206.txt").readline()

for st in "2468":
    s = s.replace(st,"0")

m = 0
for st in s.split("0"):
    if st.count("S")<35:
        continue
    if st.count("S")==35:
        m = max(m, len(st) + 1)

    for i in range(len(st)):
        if st[:i].count("S") == 36:
            m = max(m,i)
            break


print(m)