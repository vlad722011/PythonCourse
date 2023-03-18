# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в
# массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит
# число X
# *Пример:*
#    5
#    1 2 3 4 5
#    6
#    -> 5

print('Введите натуральное число:')
n = int(input())
list_a = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    Ai = int(input())
    list_a.append(Ai)
print('Итак, на вход мы имеем список:')
print(list_a)
print('Введите число "Х":')
x = int(input())
list_b = []
list_c = []
cnt_b = 0
cnt_c = 0
for k in range(len(list_a)):
    if(list_a[k] >= x):
        list_b.insert(cnt_b, list_a[k])
        cnt_b += 1
    elif(list_a[k] < x):
        list_c.insert(cnt_c, list_a[k])
        cnt_c += 1
if(len(list_b) != 0):
    index_list_b = 0
    min1 = list_b[0] - x
    for m in range(1, len(list_b)):
        min1_temp = list_b[m] - x
        if(min1_temp < min1):
            min1 = min1_temp
            index_list_b = m
else:
    min1 = 0
if(len(list_c) != 0):
    index_list_c = 0
    min2 =  x - (list_c[0])
    for j in range(1, len(list_c)):
        min2_temp = x - (list_c[j])
        if(min2_temp < min2):
            min2 = min2_temp
            index_list_c = j
else:
    min2 = 0
number = 0
if(len(list_b) != 0 and len(list_c) != 0):
    if(min1 < min2):
        number = list_b[index_list_b]
    elif(min2 < min1):
        number = list_c[index_list_c]
    elif(min1 == min2):
        number1 = list_b[index_list_b]
        number2 = list_c[index_list_c]
     
elif(len(list_b) == 0 and len(list_c) != 0):
    number = list_c[index_list_c]
elif(len(list_c) == 0 and len(list_b) != 0):
    number = list_b[index_list_b] 

index_list_a = 0  
if(min1 != min2):             
    for i in range (len(list_a)):
        if (list_a[i] == number):
            index_list_a = i
    print('Наиболее близкий элемент входящего списка к числу {} это элемент {} с индексом {}'.format(x, number, index_list_a))
else:
    for i in range (len(list_a)):
        if (list_a[i] == number1):
            index_list_a1 = i
        if (list_a[i] == number2):
            index_list_a2 = i    
    print('Наиболее близкие элементы входящего списка к числу {} это элементы {} и {} с индексами {} и {} соответсвенно'.format(x, number1, number2, index_list_a1, index_list_a2))
