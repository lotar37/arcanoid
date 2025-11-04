from random import randint

# находим список с минимальной суммой
def min_sum():
    mn = 0
    for i in range(1,len(arr)):
        if(sum(arr[i])<sum(arr[mn])):
            mn = i
    return mn

k = 20
part = 4
a = [randint(1, 10) for i in range(k)]

print(a)
arr = [[] for i in range(part)]

for i in range(k):
    j = a.index(max(a))
    k = min_sum()
    # берем самый большой элемент и кладем в список с минимальной суммой
    arr[k].append(a.pop(j))

    print([sum(a) for a in arr], arr)