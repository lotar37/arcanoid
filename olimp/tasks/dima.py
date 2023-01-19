import random as r

a = [r.randint(0, 9) for i in range(10)]
aa = [[r.randint(0, 9) for i in range(10)] for j in range(10)]

print(a,aa)


a1 = list(map(lambda x: 1 if x > 5 else 0, a))
aa1 = list(map(lambda x,y: 1 if x > 5 else 0, aa))
print(a1)
print(sum(a1))

c = sum([x + 100 if x > 5 else 0 for x in a])
print(c)