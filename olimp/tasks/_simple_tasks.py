

# ************ 1 ****************
s = input("введите строку чисел: ")

sm = 0
a = [int(st) for st in s.split()]
for n in a:
    print(n)
    sm += n

print(sm)

# ************ 2 ****************

s = input("введите строку чисел: ")

sm = 0
c = 0
a = [int(st) for st in s.split()]
for n in a:
    sm += n
    c += 1

print(sm/c)

# ************ 3 ****************

s = input("введите строку чисел: ")

sm = 0
c = 0
a = [int(st) for st in s.split()]
for n in range(0,len(a),2):
    sm += n
    c += 1

print(sm/c)


# ************ 4 ****************

s = input("введите строку чисел: ")

sm = 0
c = 0
a = [int(st) for st in s.split()]
for n in range(1,len(a),3):
    sm += n
    c += 1

print(sm/c)

# ************ 5 ****************

s = input("введите строку чисел: ")

a = [int(st) for st in s.split()]
for i in range(len(a)-1):
    if a[i+1]>a[i]:
        print(a[i+1],end=" ")




# ************ 6 ****************

s = input("введите строку чисел: ")

a = s.split()
for i in range(0,len(a)-1,2):
    a[i],a[i+1] = a[i+1],a[i]

print(" ".join(a))

