# Задача №1. В файле хранятся числа. Необходимо из файла получить четные числа, и составить список пар
#  (число, квадрат числа) Пример: 1 2 3 5 8 15 23 38 - список чисел на входе.
#  На выходе получить:[(2, 4),(8, 64),(38, 1444)]


# итоговое решение, используя готовые библиотеки языка:
data = '1 2 3 5 8 15 23 38'.split()
res = list(map(int, data))
print(res)
res = list(filter(lambda x: not x % 2, res))
res = list(map(lambda x: (x, x ** 2), res))
print(res)



# первое промежуточное решение. простым способом, используя функции.
list = [1, 2, 3, 5, 8, 15, 23, 38]
print(list)
def f(x):
    return x ** 2
def f1(list):
    list_res = []
    for i in range(len(list)):
        if (list[i] % 2) == 0:
           list_res.append(list[i])
    return list_res
list_result = []
for i in range(len(f1(list))):
    list_result.append(f(f1(list)[i]))
some_list = [(f1(list)[i], f(f1(list)[i])) for i in range (len(f1(list)))]
print(some_list)


# второе промежуточное решение используя лямбды
# допустим мы считали из файла строку, и на входе имеем следующие данные:

str = '1 2 3 5 8 15 23 38'
data = str.split()
print(data)
# опишем некоторые функции:
def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
# и собственно само решение используя лямбды и лист компрехеншн
# переменной res присваиваем результат работы функции int, которой в качестве параметра передаются строки из файла
# в результате получили массив чисел
res = select(int, data)
# переменной res присваиваем результат работы функции where, которой в качестве параметра передаются переменная res
# а из чисел из массива переменной res делаем выбоку только четных чисел, записываем при помощи лямбда выражения функцию
# в результате получили массив только из четных чисел
res = where(lambda x: not x % 2, res)
# переменной res присваиваем результат работы функции select, которой в качестве параметра передаются переменная res
# а из чисел из массива переменной res список пар(число, квадрат числа). записываем при помощи лямбда выражения функцию
# в результате получили конечный результат.
res = select(lambda x: (x, x ** 2), res)
print(res)




