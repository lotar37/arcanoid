f = open('./data/27-A2.txt')
k = int(f.readline()) * 2
n = int(f.readline())
a = [int(i) for i in f]
maximum = 0
a_sum = [a[i] + a[i+k] for i in range(len(a)-k)]
i = a_sum.index(max(a_sum))
m1, m2 = a.pop(i + k), a.pop(i)
# for i in range(len(a)-k):
#     for j in range(len(a)):
#         if i != j and i != j+k:
#             maximum = max(maximum, a[i] + a[i+k] + a[j])
print(max(a_sum) + max(a))