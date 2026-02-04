import itertools as t
s = "TCPOKA"
n = 6**5
for a in t.product(s,repeat=5):
    #print(a,"".join(a).count("O"))
    if a[0] not in 'TCA' and a[4] == "T" and "".join(a).count("O") == 2:
        print(n,a)
        break
    n -= 1
print("the end")
