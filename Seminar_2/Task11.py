# Задача 11.  Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n,  что φ(n)=A.  
# Если А не является числом Фибоначчи, выведите число -1.

print('Введите число Фибоначи:')
n = int(input())
fiboFirst = 0
fiboSecond = 1
fiboNext = fiboFirst + fiboSecond
count = 3
while (fiboNext < n):
    fiboFirst = fiboSecond
    fiboSecond = fiboNext
    fiboNext = fiboFirst + fiboSecond
    count = count + 1
    if(fiboNext == n):
        print(count)
if(fiboNext != n):
    print(-1)   

