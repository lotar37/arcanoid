f = open("data/24_1.txt")
a = f.readline()
a1 = ['A', 'O']
a2 = ['C', 'D', 'F']


def rightStep(st):
    if st[1] in ['A', 'O'] and st[0] in ['C', 'D', 'F']:
        return True
    else:
        return False


maximum = 0
mx = 0
i = 0
while i < len(a)-1:

    if rightStep(a[i:i + 2]):
        mx += 1
        i += 2
    else:
        if mx > maximum:
            maximum = mx
        mx = 0
        i += 1

print(maximum)