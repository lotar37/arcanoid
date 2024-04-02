for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (w or not y) <= (z == x)
                f2 = (w or not y) == (x <= z)
                if not f1 or not f2:
                    print(x,y,z,w,f1,f2,sep=" | ")




# x   y   z   w  f1  f2  
#     1		 1	 0
#     0	  0	 0		  0
# 0	  0	  0		 0	  0
