a = [1,2,5,10,5,10,2,50,1,2]
M = a[0]
for i in a:
    if i > M:
        M = i
    print("выдано:",i,", Mаксимальная купюра:",M)

print(M)

i = int(input("введите число"))
print(i)