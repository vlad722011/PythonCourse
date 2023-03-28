# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


print('Enter a three-digit number')
n = int(input())
if n < 0:
    n *= -1
sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
s = 'The sum of the digits that make up the number is: {}'.format(sum)
print(s)