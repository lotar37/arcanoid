from math import sqrt  as sss
cnt = 0
for i in range(45000000,50000001):
    m = 0
    a = []
    for j in range(3,int(sss(i))+1, 2):
        if i % j == 0:
            m += 1
            a.append(j)
            # print(m,j)
            if (i // j)%2 == 1:
                m += 1
                a.append(i // j)
            if i // j == j:
                m -= 1
                # print(m, j)
        if m > 5:
            break


    if m == 5:
        cnt += 1
        print(cnt , int(sss(i)), i, m, a)