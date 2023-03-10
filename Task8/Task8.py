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
