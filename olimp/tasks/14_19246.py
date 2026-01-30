
s = "0123456789abcdefghijklmno"
for i in s[::-1]:
    n = int(f"11353{i}12",25) + int(f"135{i}21",25)
    if n % 24 == 0:
        print(i,n/24)
