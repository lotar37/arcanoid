a = ">>-->"

i = 1
j = 0
p = [0]*len(a)

while i < len(a):
    if a[i] == a[j]:
        p[i] = j + 1
        i += 1
        j += 1

    else:
        if j == 0:
            i += 1
        else:
            j = p[j-1]

print(p)

tmp = ['>>-->','<--<<']

a = [[0,1,0,0,1],[0,0,0,1,1]]

s = input()


n = len(s)


count = [0,0]
for k in range(2):
    i = j = 0
    while i < n:
        if s[i] == tmp[k][j]:
            i += 1
            j += 1
            if j == len(a[k]):
                count[k] += 1
                j = a[k][j - 1]
        else:
            if j>0:
                j = a[k][j-1]
            else:
                i += 1
print(sum(count))