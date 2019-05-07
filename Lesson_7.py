"""
Задание 1.

Анализ. Исходный код я улучшил в 10-ть раз, было время - 0.19489440000000002
Стало - 0.02495449999999999

Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit
 
def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i],orig_list[i+1] = orig_list[i+1],orig_list[i]
        n += 1
    return orig_list

print ("Задание 1;")
numbers = list (range (-100,100))
random.shuffle(numbers)
print(numbers)
print()

print (bubble_sort(numbers))

#orig_list = list (range (-100,100))
#orig_list = [random.randint(-100, 100) for _ in range(500)]
#print (orig_list)
print()
#print(timeit.timeit("bubble_sort(orig_list)", \
    #setup="from __main__ import bubble_sort, orig_list", number=10))


"""
Задание 2.
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import timeit
import random

def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list

# замеры
print ("Задание 2;")
orig_list = [random.randint(0, 50) for _ in range(50)]          
print (orig_list)
print ()
print (merge_sort(orig_list))
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=10))


