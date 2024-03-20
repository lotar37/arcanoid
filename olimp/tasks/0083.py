# m, n = [int(i) for i in input().split()]
# if m > n:
#     m, n = n, m
print(2**30)
c = 0
for i in range(2**30):
    if i%2 == 0:
        c += 1