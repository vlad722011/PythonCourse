# Задача 40. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится
# число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


def count_correct_max(input_arr: list):
    count = 0
    for i in range(1, len(input_arr) - 1):
        if input_arr[i - 1] < input_arr[i] > input_arr[i + 1]:
            count += 1
    return count
len_array = int(input("Введите длинну масива: "))
array = []
for i in range(len_array):
    array.append(input(f"Введите {i + 1}-й элемент массива: "))
print(array)
print(count_correct_max(array))
