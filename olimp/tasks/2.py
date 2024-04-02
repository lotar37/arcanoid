# # ¬ (y → (x ≡ w)) ∧ (z → x )
#
# a = [x2(i) for i in range(15)]
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#
#                 if not(y => (x eq w)) and (z => x) == 1:
#                     print(x,y,z,w)
# time = input('введите время суток')
# if time == "утро":
#     print("Сейчас утреннее время")
# elif time == 'день':
#     print('Наступил день')
# elif time == 'вечер':
#     print('Наступил вечер')
# else:
#     print('Ночь. Пора спать.')

# ¬ (y → (x ≡ w)) ∧ (z → x )

# a = [x2(i) for i in range(15)]
print("x", "y", "z", "w")
print("__________________")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # ¬((x ∨ y) → (z ∧ w)) ∧ (x → w)
                if not((x == y) or (z and not w) or (not(z) and y)):
                # if not(y => (x eq w)) and (z => x) == 1:
                    print(x,y,z,w)

#
#     0	  0		0	0
#         0		0	0
#               0	0
#  