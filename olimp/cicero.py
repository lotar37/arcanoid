n = 10
a = [1]+[0]*(n+3)
for i in range(n):
    a[i+1]+=a[i]
    a[i+2]+=a[i]
    a[i+3]+=a[i]
print(a)