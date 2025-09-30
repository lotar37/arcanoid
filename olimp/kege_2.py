print("a|b|c|F")
for a in range(2):
    for b in range(2):
        for c in range(2):
            if not(not a or b) or (not a and c):
                print(a,b,c,1,sep="|")
            else:
                print(a, b, c, 0, sep="|")