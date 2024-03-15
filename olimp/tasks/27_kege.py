from math import ceil
def findDoubleMin(a):
    m = min(a)
    i1 = a.index(m)
    if i1 > 0 and i1 <len(a)-1:
        if a[i1-1] > a[i1+1]:
            i2 = i1 - 1
        else:
            i2 = i1 + 1
    elif i1 == 0:
        i2 = -1
    elif i1 == len(a) -1:
        i2 = len(a) - 2
    if i2 < i1:
        i1, i2 = i2, i1
    print(i1,i2)
    return i1

def findMin(a):
    aa = [abs(a[i+1]-a[i]) for i in range(len(a)-1)]
    i = aa.index(min(aa))
    if i != 0:
        if a[i-1] < a[i + 1]:
            i -= 1
    return i




f = open("./data/27_B.txt")
nukm = f.readline()
a = [[int(i) for i in s.split()] for s in f]
a = [[aa[0],ceil(aa[1]/36)] for aa in a]
begin = 0
step = len(a)//10



while True:
    aa = []
    for i in range(10):
        su_prev = 0
        ii = begin + i * step
        for j in range(len(a)):
            su_prev += abs(a[ii][0] - a[j][0]) * a[j][1]
        aa.append(su_prev)
    if step == 1:
        print(min(aa))
        break
    print(step, aa)
    b, b2 = findDoubleMin(aa), findMin(aa)
    print(b,b2)
    begin += b2 * step

    print(begin)
    step = step // 10



# minim = sum([aa[0]*aa[1] for aa in a])*10
# summas = []
# i = int(len(a)*5/10)
# step = 20000
# su_prev = 0
# for j in range(len(a)):
#     su_prev += abs((a[i][0] - a[j][0]) * a[j][1])
# b = 10
# while True:
#     print(step)
#     su = 0
#     i += step
#     for j in range(len(a)):
#         su += abs((a[i][0]-a[j][0])*a[j][1])
#     if su < minim:
#         minim = su
#     if su > su_prev:
#         if abs(step)>1:
#             step = -1 * (abs(step)//2) * int(step / abs(step))
#         elif  abs(step) > 1:
#             step = -1 * (abs(step) - 1) * int(step / abs(step))
#         else:
#             step *= -1
#     su_prev = su
#     if abs(step) == 1:
#         if b == 0:
#             break
#         else:
#             b -= 1
#
#
#
# print(minim)
