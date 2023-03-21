# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


print('Введите натуральное число, количество элементов первого набора чисел:')
n = int(input())
list_first = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    a_i = int(input())
    list_first.append(a_i)

print('Введите натуральное число, количество элементов второго набора чисел:')
n = int(input())
list_second = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    b_i = int(input())
    list_second.append(b_i)

# намеренно создам два дополнительных списка,для того, чтобы было 
# удобно отслеживать при выводе результаты работы программы. 
# хотя по хорошему можно обойтись входящими списками, и напрямую работать с ними

list_temp1 = list(set(list_first))
list_temp2 = list(set(list_second))

for i in range(len(list_temp2)):
    list_temp1.append(list_temp2[i])

list_result = list(set(list_temp1))
list_result.sort()

print('Итак, на вход мы имеем два набора целых чисел, возможно с повторяющимися числами')
print('Это набор № 1:')
print(list_first)
print('Это набор № 2:')
print(list_second)

print('На выходе мы получаем вот такой набор уникальных, отсортированных по возрастанию чисел:')
print(list_result)
