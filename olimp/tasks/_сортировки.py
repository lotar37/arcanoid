# простая пузырьковая
from random import randint
def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        # Проходим по каждому элементу, кроме последних i уже отсортированных
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Меняем элементы местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_list)
# print("Отсортированный список:", my_list)

# Быстрая сортировка(QuickSort)

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Опорный элемент — середина массива
        left = [x for x in arr if x < pivot]     # Левая часть (меньше опорного)
        middle = [x for x in arr if x == pivot]  # Центр (равные опорному)
        right = [x for x in arr if x > pivot]    # Правая часть (больше опорного)
        print(f"arr:{arr} left:{left} middle:{middle} right:{right}")
        return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
my_list = [randint(1,20) for _ in range(20)]
sorted_list = quick_sort(my_list)
print(sorted_list)

