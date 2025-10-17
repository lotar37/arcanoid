def worm(index,energy):
    print(index,energy)
    if index>=len(a):
        print(f"index>=len(a) index,energy=({index},{energy})")
        return 0
    if energy - a[index] < 0:
        print(f"energy - a[index] < 0 ({energy} - {a[index]} )")
        return 0
    elif index == len(a)-1:
        return energy - a[index]
    aa = [-1]
    for i in range(1, energy + 1):
        e = worm(index + i, energy - i)
        print(index + i,e,aa)
        if e>0:
            aa.append(e)

    # print(aa)
    return max(aa)

from random import randint
E = 6
a = [randint(-10, 20) if i% 7==0 else randint(-2, 5)   for i in range(5)]
print(a)
print(a,worm(0, E))


