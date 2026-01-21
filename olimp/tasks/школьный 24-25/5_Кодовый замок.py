b = int(input())
n = int(input())
good_code = [1] * b ** n
t = int(input())
for j in range(t):
    mask = input()
    sum_digits = int(input())
    for code in range(b ** n):
        saved_code = code
        s = 0
        for i in range(n):
            if mask[i] == "1":
                s += code % b
                code //= b
        if s != sum_digits:
            good_code[saved_code] = 0
print(sum(good_code))
