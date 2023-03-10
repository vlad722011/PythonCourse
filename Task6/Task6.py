# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


# Программу реализовал для билетов с любым четным количестовм цифр в номере( не обязательно 6,
# это может быть и 4 и 8 цифр в номере)

print('Enter the ticket number with an even number of digits in the number')
number = input()

lengthNumber = len(number)
count = lengthNumber // 2
i = lengthNumber - 1

sum1 = 0
while (i >= count):
    sum1 += int(number[i])
    i -= 1

sum2 = 0
while (i >= 0):
    sum2 += int(number[i])
    i -= 1

if sum1 == sum2:
    print('YES, ticket happy.')
else:
    print('NO, ticket is not lucky.')
