c = 0
for x in range(1,6):
    for y in range(-120, 130):
        if (y < (12 - x*3**0.5)) and (y > -x*3**0.5):
            c += 1
print(c)