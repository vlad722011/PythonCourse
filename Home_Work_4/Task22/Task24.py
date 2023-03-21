# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два
# соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому
# ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система
# состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один
# заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и
# с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
print()
number = random.randint(10, 20)
print('Количество кустов черники на грядке равно {}:'.format(number))
print()

berries_on_bushes = []
for i in range(number):
    count_berries = random.randint(10, 20)
    berries_on_bushes.append(count_berries)

print('Количество ягод на кустах черники, указано в следующем списке:')
print(berries_on_bushes)
print()

sum_berries_three_bushes = []
max = number_left = number_center = number_right = 0
for i in range(0, len(berries_on_bushes)):   
    left = berries_on_bushes[i-2]
    center = berries_on_bushes[i-1]
    right = berries_on_bushes[i]
    temp = left + center + right
    sum_berries_three_bushes.append(temp)
    if(temp >= max):
        max = temp
        number_left = i - 2
        number_center = i -1
        number_right = i

print('Итоговый список количества ягод расположенных на группах из трех кустов:')
print(sum_berries_three_bushes)
print()
max_count_berry = max 
print('Максимальное количество ягод на трех соседних кустах равно: {}'. format(max_count_berry))
print(max_count_berry)
print('Это кусты грядки с индексами {}, {} и {}: '. format(number_left, number_center, number_right))