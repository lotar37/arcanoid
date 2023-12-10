# n = int(input('введите число'))
# for i in range(1, n+1):
#     print("")
#     for j in range(1,10):
#         print(i, "x", j,'=', i*j)

# ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))


#  1	 2	 3	 4
# ???	???	???	???	F
# 1			     1	0
# 1				    0
#       1		1	0
#
# print("x y z ")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not((x == y) or ((y or z) <= x)):
#                 print(x,y,z)
#
#
print(sum([i for i in range(12)]))