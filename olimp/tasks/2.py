# ¬ (y → (x ≡ w)) ∧ (z → x )

# a = [x2(i) for i in range(15)]
print("x", "y", "z", "w")
print("__________________")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # ¬((x ∨ y) → (z ∧ w)) ∧ (x → w)
                if not(not(x or y) or (z and w)) and (not(x) or w):
                # if not(y => (x eq w)) and (z => x) == 1:
                    print(x,y,z,w)