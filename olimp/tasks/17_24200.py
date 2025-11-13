f = open('data/17_24200.txt')
a = [int(i) for i in f]
print(a[:100])

chet = sum([0 if i % 2 else 1 for i in a])
print(chet)
c = 0
mx = 0
for i in range(len(a)-1):
    if (a[i] * a[i+1])%chet == 0 and (a[i]//100%10 == 0 or a[i+1]//100%10 == 0):
        mx = max(mx,a[i] + a[i+1])
        c += 1
print(c,mx)