# Задача 11.  Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n,  что φ(n)=A.  
# Если А не является числом Фибоначчи, выведите число -1.

print('Введите число Фибоначи:')
n = int(input())
fibo_first = 0
fibo_second = 1
fibo_next = fibo_first + fibo_second
count = 3
while (fibo_next < n):
    fibo_first = fibo_second
    fibo_second = fibo_next
    fibo_next = fibo_first + fibo_second
    count = count + 1
    if(fibo_next == n):
        print('Число {} является {} числом в ряду Фибоначи'.format(n,count))
if(fibo_next != n):
    print('"-1", А это значит, что введенное число {} не является числом ряда Фибоначи'.format(n))   

