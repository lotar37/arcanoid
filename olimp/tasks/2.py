# ¬ (y → (x ≡ w)) ∧ (z → x )

a = [x2(i) for i in range(15)]

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):

                if not(y => (x eq w)) and (z => x) == 1:
                    print(x,y,z,w)