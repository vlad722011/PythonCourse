# 3.Создайте список из случайных чисел. Найдите второй максимум.


import random
import time

start_my = time.perf_counter()
some_list = [random.randint(-500, 500) for _ in range(0, 10000000)]
#print(some_list)
max = max(some_list)
print(max)
temp = max - 1
second_max = 0
for i in range (len(some_list)):
    if temp in some_list:
        second_max = temp
        break
    else:
        temp -= 1
print('Second_max in array = {}'.format(second_max))
end_my = time.perf_counter()
my = end_my - start_my



start_his = time.perf_counter()
input_list = some_list
#print(input_list)
first_max = input_list[0]
second_max = input_list[1]
for i in input_list:
    if i > first_max:
        second_max = first_max
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i
print('Second_max in array = {}'.format(second_max))
end_his = time.perf_counter()
his = end_his - start_his
num = my / his
print('Мой алгоритм работает в {} раз быстрее или медленнее, чем другой алгоритм.'.format(num))