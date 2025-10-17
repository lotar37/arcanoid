A = []
print(A)
for x in "012345678":
    for y in "012345678":
        s1 =  "88" + x + "4"+ y
        s2 = "7" + x + "44" + y
        n = int(s1,9) + int(s2,11)
        if n % 3 == 0:

            A.append(n//3)
            print(A)
print(min(A))