import sys
n = int(input())
a = [int(s) for s in input().split()]
mx = 1
cur = 1
for i in range(1,n):
    if a[i-1] >= a[i]:
        mx = max(cur,mx)
        cur = 1
    else:
        cur += 1
else:
    mx = max(cur, mx)
print(mx)