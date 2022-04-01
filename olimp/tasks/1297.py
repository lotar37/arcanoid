import math
M,N = [int(i) for i in input().split()]


def isSimple(n):
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

#если четное добавить 1
a = ""
if M == 2:
    a = "2"
M += (M+1)%2
for i in range(M,N+1,2):
    if isSimple(i):
        a += "\n"+str(i)
if len(a):
    print(a)
else:
    print("Absent")