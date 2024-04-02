s = open("./data/24_1147.txt").readline()
a = dict()
for i in range(1,len(s)-1):
    if s[i] == s[i+1]:
        if s[i-1] in a:
            a[s[i-1]] += 1
        else:
            a[s[i-1]] = 1
print(a,max(a))
m =["",0]

for i in a:
    if a[i] > m[1]:
        m = [i,a[i]]
print(m)

