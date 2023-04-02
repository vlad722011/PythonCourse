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
    list_= []
    res_list = []
    for i in range(1, rows + 1):
        for j in range(1,columns + 1):
            list_.append(i*j)
        res_list.append(list_)
        print(*(list_), sep=' ')
        list_ =[]
    return res_list

# Функция, находящая в полученной таблице элемент, по заданным номерам строки и столбца
def find_elem(some_list , row, col):
    return some_list[row-1][col-1]

print('Исходная таблица -:')
print()
result_list = print_table(count_rows, count_columns)
num = find_elem(result_list, number_row, number_col)
print()
print(f'Элемент таблицы с номером строки {number_row} и номером столбца {number_col}, равен -: {num}')
print()



# Вариант решения задачи вторым способом, как требовалось по условию, используя в качестве 
#  аргументов одной функции, другую функцию.



print('Вариант решения №2 (используя одну функцию в качестве аргумента для другой): ')
print()
print('Исходная таблица -:')
print()

# Функция возвращает список, элементами которого являются списки - списки элементов строк входящей таблицы,
# в которой будем искать элемент по заданным номерам строки и столбца
def operation(rows, columns):
    res_list =[]
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
    return some_list[row-1][column -1]

number = print_operation_table(operation, number_row, number_col)
print()
print(f'Элемент таблицы с номером строки {number_row} и номером столбца {number_col}, равен -: {number}')