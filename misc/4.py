a = [0]*1000
for i in range(10,1001):
    j = bin(i)[2:]
    print(j)
    j = j.replace("1","*")
    j = j.replace("0", "1")
    j = j.replace("*", "0")
    print(j)
    print("------------")
    index = i - int(j,2)
    a[index] = 1
print(sum(a))

aa = []
for i in range(100, 3001):
    j = i - int(bin(i)[3:], 2)
    if j not in aa:
        aa.append(j)
print(aa)
