from random import randint

n = 10
a = [randint(1, 100) for _ in range(n)]
# n = int(input())
# a = [int(s) for s in input().split()]
a.sort()
a = [0] + a + [100]
dp = [0]+[a[i + 1] - a[i] for i in range(n - 1)]

dp_a = [0] + [1] + [0] * (n - 3) + [1]

for i in range(2, n - 1):
    dp_a[i] = dp[i - 1] + dp[i - 2]
    if dp_a[i - 1] == 0:
        dp_a[i] = 1
    elif dp_a[i-2] == 1 and dp_a[i - 1] == 1 :
        dp_a[i] = 0
    else:
        if a[i] >= a[i + 1]:
            dp_a[i] = 0
        elif a[i] + a[i + 2] <= a[i + 1] + a[i + 3] :
            dp_a[i] = 0
        else:
            dp_a[i] = 1
print(a, dp, dp_a, sep='\n')

# d  =  [0 for i in range(n)]
#
# d[1] = a[1]-a[0]
# d[n-1] = a[n-1]-a[n-2]
# for i in range(2, n-2):
#     print(d)
#     if d[i]:
#         continue
#     if a[i] - a[i-1] <= a[i+1] - a[i]:
#         d[i] = a[i] - a[i-1]
#     else:
#         d[i+1] = a[i+1] - a[i]
#     # if d[i] > 0 and d[i-1] > 0 and d[i-2] and i>2 > 0:
#     #     d[i-1] = 0
#
# print(sum(d))
# print(a)
# print(d)
