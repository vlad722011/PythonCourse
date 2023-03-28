import time

fibo_0 = 0
fibo_1 = 1
fibo_prev = fibo_0 + fibo_1
fibo_next = fibo_1 + fibo_prev
fibo_list_result = [fibo_0, fibo_1, fibo_prev, fibo_next]
#print('Введите натуральное число:')
#n = int(input())

n = 50

start = time.perf_counter()

for i in range(n - 4):
    fibo_list_result.append(fibo_prev + fibo_next)
    fibo_temp = fibo_next
    fibo_next = fibo_next + fibo_prev
    fibo_prev = fibo_temp
print('Последовательность Фибоначи: - {}'.format(fibo_list_result))
print('N-ый элемент последовательности Фибоначи равен: {}'.format(fibo_list_result[-1]))

end = time.perf_counter()
time_it = end - start

# Вариант программы с рекурсией

start_rec = time.perf_counter()

list_start = [0, 1]


def fibo_recursive(n):
    fibo_list = list_start
    fibo_list.append(fibo_list[-2] + fibo_list[-1])
    if n == 3:
        return fibo_list
    elif n != 3:
        return fibo_recursive(n - 1)


list_end = fibo_recursive(n)
print('Итоговый список чисел Фибоначи: - {}'.format(list_end))
print('N-ый элемент последовательности Фибоначи равен: {}'.format(list_end[-1]))

end_rec = time.perf_counter()
time_rec = end_rec - start_rec

print('отличия в скорости в {} раз'.format(time_rec / time_it))
