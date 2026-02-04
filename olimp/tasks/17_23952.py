f = open("./data/17_23952.txt")
a = [int(i) for i in f]

mx = max([i if i%100 == 93 else 0 for i in a])
print(mx)
n = []
for i in range(len(a)-1):
    if (a[i] < mx < a[i+1]) or (a[i+1] < mx < a[i]):
        if (str(a[i])[0] == "9") or (str(a[i+1])[0] == "9"):
            n.append(max(a[i],a[i+1]))
print(len(n),sum(n))