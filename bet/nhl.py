n = 0
for i in range(10):
    for j in range(10):
        if i+j >5 and i +j < 10 and abs(i-j)<5:
            n += 1
            print(n," - " ,i,":",j)
