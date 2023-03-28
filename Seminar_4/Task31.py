# 1.Создайте список из случайных чисел. Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше всех из своих соседей).

import random

some_list = [random.randint(-10, 20) for _ in range(0, 15)]
print(some_list)
new_list = []
new_list_index = []
for i in range(len(some_list)-1):
    if ((some_list[i] > some_list[i+1]) and (some_list[i] > some_list[i-1])):
        max = some_list[i]
        number = i
        new_list.append(max)
        new_list_index.append(i)

#print(new_list)
#print(new_list_index)
#print(max)
print(number)



import random
input_list = [random.randint(1, 100) for _ in range(10)]
print(input_list)
for i in range(len(input_list) - 2, 0, -1):
    if input_list[i - 1] < input_list[i] > input_list[i + 1]:
        print(i)
        break