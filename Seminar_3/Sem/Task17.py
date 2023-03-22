# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

list_1 = []
list_len = int(input('Введите количество элементов списка: '))
for i in range(list_len):
    list_1.append(int(input(f'Введите {i+1} число ')))
print(list_1)
set_1 = set(list_1)
print(len(set_1))