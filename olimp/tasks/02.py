# (w→y) ∧ (¬y ≡ x) ∧ (x ∨ z)

#
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (w<=y) and (not y == x) and (x or z):
#                     print(x,y,z,w)

from copy import deepcopy
a = [1,2,3, [1,2,3]]

a1 = a
b = deepcopy(a)
print(id(a), id(a1), id(b))
if id(a) == id(a1):
    print('equal objects')

a[3][2] = 555

print(a, a1, b)