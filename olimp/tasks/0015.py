n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

a = [[a[i][j] if i > j else 0 for j in range(len(a[i]))] for i in range(len(a))]

print(sum([sum(aa) for aa in a]))