# Задача №3. Последовательностью Фибоначчи называется последовательность чисел a, a1, ..., an, ..., где a0 = 0,
# a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи Input: 7 Output: 21
# Задание необходимо решать через рекурсию


# сначала решим итеративным способом
fibo_list_start = [0, 1, 1, 2]
fibo_0 = 0
fibo_1 = 1
fibo_prev = fibo_0 + fibo_1
fibo_next = fibo_1 + fibo_prev
fibo_list_result = fibo_list_start
print('Введите натуральное число:')
n = int(input())
for i in range(n-4):
    fibo_list_result.append(fibo_prev + fibo_next)
    fibo_temp = fibo_next
    fibo_next = fibo_next + fibo_prev
    fibo_prev = fibo_temp
print('Последовательность Фибоначи: - {}'.format(fibo_list_result))
print('N-ый элемент последовательности Фибоначи равен: {}'.format(fibo_list_result[-1]))


# потом решим рекурсией
print('Введите натуральное число:')
n = int(input())
list_start = [0, 1]
def fibo_recursive(n):
    fibo_list = list_start
    fibo_list.append(fibo_list[-2] + fibo_list[-1])
    if n == 3:
        return fibo_list
    elif n!= 3:
        return fibo_recursive(n - 1)
list_end = fibo_recursive(n)
print(list_end)
print(list_end[-1])


# еще вариант с рекурсией
def fibonachi_recursion(serial_number):
    if serial_number == 1:
        return 0
    if serial_number == 2:
        return 1
    return fibonachi_recursion(serial_number - 1) + fibonachi_recursion(serial_number - 2)
print(fibonachi_recursion(15))

# еще вариант с итеративным решением
def fibonachi_iteration(serial_number):
    first = 0
    second = 1
    if serial_number == 1:
        return first
    if serial_number == 2:
        return second
    count = 2
    while serial_number != count:
        third = first + second
        first = second
        second = third
        count += 1
    return third
print(fibonachi_iteration(15))
