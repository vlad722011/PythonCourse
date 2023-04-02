# Если ты много лет подряд был воином Белой розы, если ты не раз участвовал в кровопролитных битвах между индейцами
# и бледнолицыми, если ты, наконец, был разведчиком союзников во второй мировой войне, то ты научился двум вещам:
# ничему не удивляться и уметь молчать, когда надо.
# Напишите программу, которая найдет отличия между индейцами и бледнолицыми (или Белой розой и Красной розой,
# кто их разберет!).
# Из каждых двух наборов целых чисел выбрать общие, оканчивающиеся на 1 или 3, без повторений. Вывести в порядке
# убывания через &, окруженный пробелами.
# Формат ввода
# Вводится число n – количество наборов из двух строк, в которых целые числа записаны через пробел.
# Затем 2 * n строк с целыми числами.
# Формат вывода
# Вывести n строк, в которых записаны определенные по указанному правилу числа через &, окруженный пробелами
#
# Ввод
# 3
# 9 28 21 23 12 41
# 6 21 18 26 41 18 23 53
# 18 4 25 31 15 20 31 1
# 2 13 10 28 12
# 10 31 23 13 121 17 9 18
# 31 9 3 10 121 4 14 21

# вывод
# 41 & 23 & 21
# 121 & 31

list_1 = [9, 28, 21, 23, 12, 41]
list_2 = [6, 21, 18, 26, 41, 18, 23, 53]
list_3 = [18, 4, 25, 31, 15, 20, 31, 1]
list_4 = [2, 13, 10, 28, 12]
list_5 = [10, 31, 23, 13, 121, 17, 9, 18]
list_6 = [31, 9, 3, 10, 121, 4, 14, 21]

import random

print('Введите количество пар строк:')
n = int(input())

i


def palefaces_and_indians(list_one, list_two):
    temp_list1 = list(filter(lambda x:  (x % 10 == 1 or x % 10 == 3), list_one))
    temp_list2 = list(filter(lambda x:  (x % 10 == 1 or x % 10 == 3), list_two))
    res_list =[]
    for i in temp_list1:
        if i in temp_list2:
            res_list.append(i)
    res_list.sort(reverse = True)
    str_ = ''
    if len(res_list) != 0:
        for i in range(len(res_list) - 1):
            str_ += str(res_list[i]) + ' & '
        str_ += str(res_list[-1])
    else:
        return ''
    return str_

print(palefaces_and_indians(list_1, list_2))
print(palefaces_and_indians(list_3, list_4))
print(palefaces_and_indians(list_5, list_6))



print('Введите количество пар строк:')
n = int(input())
print('Введите строки, в которых числа разделены пробелами:')
#some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for i in range(2 * n)]
#print(some_list)
some_list = []
for _ in range(2 * n):
    temp_list = []
    for i in input().split():
        if i[-1] in('1', '3'):
            temp_list.append(i)
    some_list.append(temp_list)
#print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ')