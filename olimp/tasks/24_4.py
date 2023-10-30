f = open('./data/24_4.txt').readline()
a = f.split('XZZY')
m = 0
for i in a:
    if len(i) > m:
        m = len(i)
print(m+6)