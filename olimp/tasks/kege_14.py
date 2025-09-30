def convert(s,k):
    d = "0123456789ABCDEFGHIJ"
    n = 0
    for i in range(len(s)):
        n += int(d.index(s[i]))*k**(len(s)-i-1)
    return n

m = 0
for i in "0123456789ABCDEFGHIJ":
    s1 = "A3"+i + "74"
    s2 = i + "40846"
    n = convert(s1,19) + convert(s2,19)
    if n % 9 == 0:
        m = max(m, n //9)
print(m)
print(convert("11A",19))