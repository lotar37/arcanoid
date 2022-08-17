from random import randint
import time



a = [randint(1,1000) for i in range(10000)]
maximum = 0
start_time = time.time()

max_arr = [0,0,0,0,0]
null_second_max = -1
for i in a:
    index = i % 5

    if i > max_arr[index]:
        if not index:
            null_second_max = max_arr[index]
        max_arr[index] = i
print(max_arr)
print(max(null_second_max + max_arr[0], max_arr[1] + max_arr[4], max_arr[2] + max_arr[3]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

a.sort(reverse=True)
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if a[j] + a[i] > maximum:
            if (a[j] + a[i]) % 2 == 0:
                maximum = a[j] + a[i]
        else:
            break
print(maximum)
print("--- %s seconds ---" % (time.time() - start_time))