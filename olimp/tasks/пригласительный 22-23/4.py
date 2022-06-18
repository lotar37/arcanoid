d = 88888888888888888844444444
c = 0
while d > 0:
    s = str(d)
    c += 1
    for i in s:
        if i in "13579":
            d -= 1
            break
    d //= 2
print(c)