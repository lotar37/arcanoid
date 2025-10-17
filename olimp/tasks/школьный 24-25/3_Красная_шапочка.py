def worm(index,energy):
    if index>=len(a):
        return False
    if energy - a[index] < 0:
        return False
    elif index == len(a)-1:
        return energy - a[index]
    aa = []
    for i in range(1, energy + 1):
        e = worm(index + i, energy - i)
        if e:
            aa.append(e)
    return max(aa)

from random import randint
E = 12
a = [randint(-10, 20) if i% 7==0 else randint(-2, 5)   for i in range(10)]
print(a,worm(0, E))


