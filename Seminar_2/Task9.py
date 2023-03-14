# Задача 9.  По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N(произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

#print('Enter an integer, non-negative number:')
print('Введите целое неотрицательное число:')
n = int(input())
count = 1
factorial = 1

while (count < n):
    factorial = factorial * (count + 1)
    count += 1
s = 'Факториал числа {} равен {}'.format(n, factorial)
print(s)