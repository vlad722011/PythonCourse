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
    if list_a[i] == x:
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