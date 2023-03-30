f = open('17.txt')
l = [int(i) for i in f]
count = mx = 0
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        s = abs(l[i] - l[j])
        if s % 60 == 0:
            count += 1
            if s > mx:
                mx = s

print(count, mx)
