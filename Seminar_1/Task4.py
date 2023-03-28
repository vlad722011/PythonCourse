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
 



    