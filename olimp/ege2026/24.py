s = open("./data/24_22359.txt").readline()
alfabet = "0123456789ABCDE"

def convert(N):
    N = N[0:0:-1]
    n = 0
    for i in range(len(N)):
        n += N[i]*15**i
    return n
s1 = ""
mx = 0
for i in range(len(s)):
    if s[i] in alfabet:
        s1 += s[i]
    else:
        c = convert(s1)
        if c % 5 == 0 and c > mx: