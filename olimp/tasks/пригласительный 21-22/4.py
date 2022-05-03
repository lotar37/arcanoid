a = 15
b = 11
c = 4
d = 0
if a < b:
    a, b = b, a

num0 = a - 1

if c == a:
    if d:
        ret = 1
    else:
        ret =  b
elif c == b:
    if d:
        ret = 1
    else:
        ret =  a
else:
    if c>b:
        if d:
            ret = a - c + 1
        else:
            ret = c -1
    else:
        if d:
            ret = b - c + 1
        else:
            ret = a -1 - (b - c)

print(ret)

