# n = int(input())
# a = [[int(s) for s in input()] for i in range(n)]
def печать(n):
    return n * 2

print(печать())
n = 3
a = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 1, 1]
]
dp = [[0]*n for _ in range(n)]
mx = 0
for i in range(n):
    dp[0][i] = a[0][i]
    if dp[0][i] > mx:
        mx = dp[0][i]

for i in range(n):
    dp[i][0] = a[i][0]
    if dp[i][0] > mx:
        mx = dp[i][0]

for i in range(1, n):
    for j in range(1, n):
        if a[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
            if dp[i][j] > mx:
                mx = dp[i][j]

print(mx**2)