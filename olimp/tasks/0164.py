def find_root(s):
    summ = 10
    while summ > 9:
        a = [int(i) for i in s]
        summ = sum(a)
        s = str(summ)

    return summ

s = input()

if s == "0":
    s = "1"

s = s.replace("0","").strip()


s = "0"+s+"0"

for i in range(1,len(s)):
    if find_root(s[:i]) == find_root(s[i:]):
        print("YES")
        break
else:
    print("NO")


print(sum([[int(j) if j>i else 0 for j in input().split()]  for i in range(5)]))
