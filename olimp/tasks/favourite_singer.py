# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)
n = int(input())
S = input()
arr = [0]*200001
a = [i for i in S.split()]
for i in a:
    arr[int(i)] = S.count(i)
M = max(arr)
arr = [str(i) for i in arr]
print(" ".join(arr).count(str(M)))