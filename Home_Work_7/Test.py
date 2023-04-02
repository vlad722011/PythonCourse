# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Ввод:
# print_operation_table(lambda x, y: x * y)

# Запрашиваем у пользоваткля входящие данные:

print('Введите количество строк таблицы: ')
count_rows = int(input())
print('Введите количество столбцов таблицы: ')
count_columns = int(input())
print('Введите номер строки таблицы, в которой находится искомый элемент: ')
number_row = int(input())
print('Введите номер столбца таблицы, в котором находится искомый элемент ')
number_col = int(input())


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
print(f'Элемент таблицы с номером строки {number_row} и номером столбца {number_col}, равен -: {number}')