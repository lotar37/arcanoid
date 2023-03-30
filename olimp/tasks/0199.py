# Необходимо сократить дробь, записанную в римской
# системе счисления. Напомним, что в римской записи
# используются символы M, D, C, L, X, V и I.

prs = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def parse(str):
    a = [prs[i] for i in str]
    s = i = 0
    while i < len(a)-1:
        if a[i] < a[i + 1]:
            s -= a[i]
        else:
            s += a[i]
        i += 1
    s += a[i]
    return s

aa = [parse(s) for s in input().split("/")]
print(aa)