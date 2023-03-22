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

s = 'The sum of the digits that make up the number is: ->  {} '.format(sum)
print(s)


#  Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
#  Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
#  если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#   *Пример:*
#   6 -> 1  4  1
#   24 -> 4  16  4
#   60 -> 10  40  10

print('Enter how many cranes the children made?')
sum = int(input())
p = s = (sum // 3) // 2
k = (p + s) * 2
kate = 'Kate made {} cranes.'.format(k)
petr = 'Petr made {} cranes.'.format(p)
sergey = 'Sergey made {} cranes.'.format(s)
print(petr)
print(kate)
print(sergey)
 


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



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

print('Enter the first number, the number "n" the size of the chocolate bar.')
n = int(input())
print('Enter the second number, the number "m" the size of the chocolate bar.')
m = int(input())
print('Enter the number "k"- the number of slices that we want to break off from a chocolate bar')
k = int(input())

if n < m:
    min = n
else:
    min = m

if ((((k % n) == 0) or (k % m) == 0) & (k >= min)):
    print('YES, so many slices can be broken off')
else:
    print('NO, such a number of slices cannot be broken off')
