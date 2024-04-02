f = open('./data/26_demo.txt')
W = int(f.readline().split()[0])
a = [int(i) for i in f]
a.sort()
print(a[:100])
for i in range(len(a), 0, -1):
    if sum(a[:i]) < W:
        break
print(i,sum(a[:i]),max(a[:i]))
d = W - sum(a[:i]) + max(a[:i])
print(d)
m = 0
for j in range(i,len(a)):
    if a[j] < d:
        m = a[j]
print(i,m)
