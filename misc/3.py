y, x = 987654321, 123456789
delta = 17636680
y, x = y - delta, x - delta
for i in range(100):
    x -= 1
    y -= 1
    print(x, y, y // x, y - (y // x) * x, 123456789 // 7)
