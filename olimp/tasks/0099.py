idx = [int(i) for i in input().split()]
a = []

count_arr = [[], []]


def step(d, count):
    i, j, k = d
    global a, idx
    if k < idx[2] - 1:
        if a[i][j][k + 1] == ".":
            a[i][j][k + 1] = count
            count_arr[count].append([i, j, k + 1])
    if k > 0:
        if a[i][j][k - 1] == ".":
            a[i][j][k - 1] = count
            count_arr[count].append([i, j, k - 1])
    if j < idx[1] - 1:
        if a[i][j + 1][k] == ".":
            a[i][j + 1][k] = count
            count_arr[count].append([i, j + 1, k])
    if j > 0:
        if a[i][j - 1][k] == ".":
            a[i][j - 1][k] = count
            count_arr[count].append([i, j - 1, k])
    if i < idx[0] - 1:
        if a[i + 1][j][k] == ".":
            a[i + 1][j][k] = count
            count_arr[count].append([i + 1, j, k])


for i in range(idx[0]):
    a.append([[k for k in input()] for j in range(idx[1])])
    if i < idx[0] - 1:
        s = input()

ii = 1
count_arr.append([])
step([0, 0, 0], 2)
print(a)
while ii < 10:
    ii += 1

    count_arr.append([])
    print(ii, count_arr)
    for d in count_arr[ii]:
        step(d, ii + 1)

print(a)
