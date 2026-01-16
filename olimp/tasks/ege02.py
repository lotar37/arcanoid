print("x   y   z   w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # (x → y) ≡ (y → z)) ∧ (y ∨ w)
                if ((x<=y) == (y<=z)) and (y or w):
                    print(x,y,z,w,sep=" | ")




# x   y   z   w  f1  f2  
#     1		 1	 0
#     0	  0	 0		  0
# 0	  0	  0		 0	  0
