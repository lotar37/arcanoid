K, N= [int(i) for i in input().split()]

a = [0 if i else 1 for i in range(N+1)]

for i in range(len(a)):
    for j in range(1, K+1):
        try:
            a[i+j] += a[i]
        except:
            pass
print(max(a))