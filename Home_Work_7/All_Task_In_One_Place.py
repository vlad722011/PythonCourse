# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из
# одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам



print('Введите стихотворение Винн-Пуха:')
str_ = input()
dict_puh_eng = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5, 'Y': 6, 'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'y': 6}
dict_puh_rus = {'А': 1, 'Е': 2, 'Ё': 3, 'И': 4, 'Й': 5, 'О': 6, 'У': 7, 'Ы': 8, 'Э': 9, 'Ю': 10, 'Я': 11,
                'а': 1, 'е': 2, 'ё': 3, 'и': 4, 'й': 5, 'о': 6, 'у': 7, 'ы': 8, 'э': 9, 'ю': 10, 'я': 11}


# Вариант решения задачи простым, более понятным способом, используя циклы.

some_list = str_.split(' ')
count = 0
vowel_count_list = []
for i in range(len(some_list)):
    temp = some_list[i]
    for i in temp:
        if i in dict_puh_eng or i in dict_puh_rus:
            count += 1
    vowel_count_list.append(count)
    count = 0
print('Решение №1 : ')
print(f'Список количества гласных букв в каждой фразе стихотворения - {vowel_count_list}')
vovel_count_set = set(vowel_count_list)
if len(vovel_count_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')


# вариант решения задачи используя функции высшего порядка

count_vovel_list = []
for i in range(len(some_list)):
    count_vovel_list.append(len(list(filter(lambda x: x in dict_puh_rus or x in dict_puh_eng, some_list[i]))))
print('Решение №2 : ')
print(f'Список количества гласных букв в каждой фразе стихотворения - {count_vovel_list}')
if len(set(count_vovel_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')

    # Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
    # которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
    # Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
    # Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

    # Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, например,
    # как у операции умножения.

    # Ввод:
    # print_operation_table(lambda x, y: x * y)

    # Вывод:
    # 1 2 3 4 5 6
    # 2 4 6 8 10 12
    # 3 6 9 12 15 18
    # 4 8 12 16 20 24
    # 5 10 15 20 25 30
    # 6 12 18 24 30 36

    # Запрашиваем у пользоваткля входящие данные:

print('Введите количество строк таблицы: ')
count_rows = int(input())
print('Введите количество столбцов таблицы: ')
count_columns = int(input())
print('Введите номер строки таблицы, в которой находится искомый элемент: ')
number_row = int(input())
print('Введите номер столбца таблицы, в котором находится искомый элемент ')
number_col = int(input())
print()

print('Вариант решения №1 (более понятным простым способом, вызывая функции последовательно): ')
print()


# функция выводящая на экран таблицу:
def print_table(rows, columns):
    list_ = []
    res_list = []
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            list_.append(i * j)
        res_list.append(list_)
        print(*(list_), sep=' ')
        list_ = []
    return res_list


# Функция, находящая в полученной таблице элемент, по заданным номерам строки и столбца
def find_elem(some_list, row, col):
    return some_list[row - 1][col - 1]


print('Исходная таблица -:')
print()
result_list = print_table(count_rows, count_columns)
num = find_elem(result_list, number_row, number_col)
print()
print(f'Элемент таблицы с номером строки {number_row} и номером столбца {number_col}, равен -: {num}')
print()
print('Вариант решения №2 (используя одну функцию в качестве аргумента для другой): ')
print()
print('Исходная таблица -:')
print()


# Функция возвращает список, элементами которого являются списки - списки элементов строк входящей таблицы,
# в которой будем искать элемент по заданным номерам строки и столбца
def operation(rows, columns):
    res_list = []
    temp_list = []
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            num = lambda i, j: i * j
            temp_list.append(num(i, j))
        res_list.append(temp_list)
        temp_list = []
    return res_list


# Собственно функция, которая взвращает элемент таблицы по его номерам строки и столбца.
# Сама функция в качестве одного из аргументов принимает другую функцию.

def print_operation_table(func, row, column):
    some_list = operation(count_rows, count_columns)
    for i in range(count_rows):
        print(*(some_list[i]), sep=' ')
    return some_list[row - 1][column - 1]


number = print_operation_table(operation, number_row, number_col)
print()
print(f'Элемент таблицы с номером строки {number_row} и номером столбца {number_col}, равен -: {number}')