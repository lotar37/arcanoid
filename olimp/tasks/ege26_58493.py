f = open("data/26_58493.txt")
a = [[int(d.split()[0]),int(d.split()[1]),d.split()[2]] for d in  f.readlines()]

a = sorted(a, key= lambda data: data[0])

def find_place(a):
    for i in range(len(a)):
        if a[i] <= 0:
            return i
    else:
        return -1

a_A = [0]*80
a_B = [0]*20
time = a[0][0]
result = [0,0]
for aa in a:
    curtime = aa[0]
    a_A = [t - (curtime - time) for t in a_A]
    a_B = [t - (curtime - time) for t in a_B]
    if aa[2] == "A":
        i = find_place(a_A)
        if i > -1:
            result[0] +=1
            a_A[i] =  aa[1]
        else:
            i = find_place(a_B)
            if i > -1:
                a_B[i] = aa[1]
                result[0] += 1
            else:
                result[1] += 1
    else:
        i = find_place(a_B)
        if i > -1:
            a_B[i] = aa[1]
        else:
            result[1] += 1

    time = curtime

    print(time,a_B)


print(result)