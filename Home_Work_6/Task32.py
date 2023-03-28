# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

mini = int(input('Введите минимум диапазона: '))
maxi = int(input('Введите максимум диапазона: '))

input_list = [random.randint(1,100) for i in range(30)]
print('Входящий массив: {}'.format(input_list))
index_list = []
for i in range(len(input_list)):
    if mini <= input_list[i] <= maxi:
        index = i
        index_list.append(index)
print('Массив индексов элементов, принадлежащих заданному диапазону: {}'.format(index_list))
