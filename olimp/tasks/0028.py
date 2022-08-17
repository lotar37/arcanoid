x1, y1, x2, y2 = 0, 0, 0, 1
point = [10, 10]
# x1, y1, x2, y2 = 0, 0, 1, 0
# point = [10, 10]

# x1, y1, x2, y2 = [int(i) for i in input().split()]
# point = [int(i) for i in input().split()]



if x1 > x2:
    x1, x2, y1, y2 = x2, x1, y2, y1

if x1 == x2:
    x = x1 - (point[0] - x1)
    y = point[1]
elif y1 == y2:
    y = y1 - (point[1] - y1)
    x = point[0]
else:
    k1 = (y2 - y1)/(x2 - x1)
    c1 = y1 - k1 * x1

    k2 = -1/k1
    c2 = point[1] - k2 * point[0]

    x_cross = (c2 - c1)/(k1 - k2)
    y_cross = k1 * x_cross + c1

    x = x_cross - (point[0] - x_cross)
    y = y_cross - (point[1] - y_cross)
print(x,y)


