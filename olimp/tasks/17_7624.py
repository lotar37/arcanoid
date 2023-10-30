def sum_cort(a):
    return a['X'] + a['Y'] + a['Z']


f = open('./data/24_7624.txt')
s = f.read()
count = 0
c = 0
maks = 0
a_xyz = {'X': 0, 'Y': 0, 'Z': 0}
xyz = "XYZ"
for i in range(len(s)):
    if s[i] in xyz:
        a_xyz[s[i]] = 1
    if sum_cort(a_xyz) == 2:
        maks = max(maks, c)
        a_xyz = {'X': 0, 'Y': 0, 'Z': 0}

        a_xyz[s[i]] = 1
        c = 0
    c += 1
else:
    maks = max(maks, c)
print(maks)
