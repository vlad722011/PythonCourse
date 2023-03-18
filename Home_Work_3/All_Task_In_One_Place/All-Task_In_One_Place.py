# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма
# (без count). Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно
# отличается.
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import time
print('Введите натуральное число:')
n = int(input())
list_a = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    Ai = int(input())
    list_a.append(Ai)
print('Введите значение элемента списка, которое будем искать, и считать сколько раз оно встречается в списке:')
x = int(input())
print('Будем искать в списке число {}, и также посчитаем сколько раз оно в списке встречается.'.format(x))
print('Итак, на вход мы имеем список:')
print(list_a)
print('Решаем задачу собственным методом:')
start1 = time.time() 
cnt = 0
for i in range(n):
    if(list_a[i] == x):
        cnt += 1
print('Число {} встречается в списке {} раз'.format(x, cnt))
time.sleep(2)
end1 =time.time()
execution_time1 = start1 - end1
print('Теперь для решения задачи используем для подсчета метод "count"')
start2 =time.time()
count = list_a.count(x)
print('Число {} встречается в списке {} раз: '.format(x, count))
time.sleep(2)
end2 =time.time()
execution_time2 = start2 - end2
print('Время исполнения алгоритма собственным методом равно {}'.format(execution_time1))
print('Время исполнения алгоритма методa "count" равно {}'.format(execution_time2))




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
list = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    a_i = int(input())
    list.append(a_i)
print('Итак, на вход мы имеем список:')
print(list)
print('Введите число "Х":')
x = int(input())
def find_elem(list):
    list.sort()
    if(x >=  list[len(list) -1]):
        number1 = number2 = (list[len(list) -1])           
    elif(x <= list[0]):
        number1 = number2 = (list[0])    
    else:
        index = 0
        n = list[index] - x
        while(n < 0):
            index += 1
            n = list[index] - x           
        number1 = (list[index-1])
        number2 = (list[index]) 
    if(number1 == number2):
        print('Ближайшее к числу {} в списке: - это число {}'.format(x, number1))
    else:
        abs1 = abs(number1 - x)
        abs2 = abs(number2 - x)
        if(abs1 == abs2):
            print('Ближайшие к числу {} в списке: - это числа {} и {}'.format(x, number1, number2))
        elif(abs1 < abs2):
            print('Ближайшее к числу {} в списке: - это число {}'.format(x, number1)) 
        else:
            print('Ближайшее к числу {} в списке: - это число {}'.format(x, number2))
find_elem(list)


# Приведенное выше решение задачи 18 - это финальное решение. Ниже можно отследить, так сказать 
# "эволюцию решения задачи", когда первым делом удалсоь в принципе получить решение любым способом,
# лишь бы задача была решена. Ну а далее было решение 2, уже отлично оптимизированное. И затем 
# финальное решение, приведенное выше. Ниже будут приложены промежуточные решения (не оптимальные). 

# Первое промежуточное решение (самое не оптимальное):

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

# Второе решение задачи (уже вполне себе отличное, с моей точки зрения):

print('Введите натуральное число:')
n = int(input())
list = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    Ai = int(input())
    list.append(Ai)
print('Итак, на вход мы имеем список:')
print(list)
list.sort()
print('Введите число "Х":')
x = int(input())
delta1 = delta2 = 0
first_left = first_right = 0
for j in range(len(list)):
    n = list[j] - x
    if (j != 0 and n >= 0):
        first_right = list[j]
        first_left = list[j-1]
        delta1 = first_right - x  
        delta2 = x - first_left 
        if (delta1 == delta2):
            print('Ближаишие к числу {} в списке: - это числа {} и {}'.format(x, first_left, first_right))
            break
        elif(delta1 < delta2):
            print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_right))
            break
        else:
            print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_left))
            break
    elif(j == 0 and n >= 0):
        first_right = list[0]
        print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_right))
        break
    elif(j == (len(list)-1) and n <= 0):
        first_left = list[j]
        print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_left))
        break


    # *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только 
# английские, либо только русские буквы.
#    *Пример:*
#    ноутбук
#    12

dictionary_english = {
    'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1,
    'L' : 1, 'N' : 1, 'S' : 1, 'T' : 1, 'R' : 1,
    'D' : 2, 'G' : 2,
    'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
    'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
    'K' : 5,
    'J' : 8, 'X' : 8,
    'Q' : 10, 'Z' : 10
}
dictionary_russian = {
    'А' : 1, 'В' : 1, 'Е' : 1, 'И' : 1, 'Н' : 1,
    'О' : 1, 'Р' : 1, 'С' : 1, 'Т' : 1, 
    'Д' : 2, 'К' : 2, 'Л' : 2, 'М' : 2, 'П' : 2, 'У' : 2,
    'Б' : 3, 'Г' : 3, 'Ё' : 3, 'Ь' : 3, 'Я' : 3,
    'Й' : 4, 'Ы' : 4, 
    'Ж' : 5, 'З' : 5, 'Х' : 5, 'Ц' : 5, 'Ч' : 5,
    'Ш' : 8, 'Э' : 8, 'Ю' : 8,
    'Ф' : 10, 'Щ' : 10, 'Ъ' : 10
}
print('Введите слово на английском или русском языке:')
s = input().upper()   
k = len(s)
sum = 0
for i in range(k):
    letter= s[i]
    if (letter in dictionary_english):
        number = dictionary_english[letter]
        sum += number 
    elif (letter in dictionary_russian):
        number = dictionary_russian[letter]
        sum += number      
print(sum) 
print('Стоимость введенного слова равна {}.'.format(sum)) 