# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в
# массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит
# число X
# *Пример:*
#    5
#    1 2 3 4 5
#    6
#    -> 5

print('Введите натуральное число:')
n = int(input())
list = list()
for i in range(n):
    print('Введите элемент списка с индексом {}:'.format(i))
    a_i = int(input())
    list.append(a_i)
print('Итак, на вход мы имеем список:')
print(list)
print('Введите число "Х":')
x = int(input())
def find_elem(list):
    list.sort()
    if(x >=  list[len(list) -1]):
        number1 = number2 = (list[len(list) -1])           
    elif(x <= list[0]):
        number1 = number2 = (list[0])    
    else:
        index = 0
        n = list[index] - x
        while(n < 0):
            index += 1
            n = list[index] - x           
        number1 = (list[index-1])
        number2 = (list[index]) 
    if(number1 == number2):
        print('Ближайшее к числу {} в списке: - это число {}'.format(x, number1))
    else:
        abs1 = abs(number1 - x)
        abs2 = abs(number2 - x)
        if(abs1 == abs2):
            print('Ближайшие к числу {} в списке: - это числа {} и {}'.format(x, number1, number2))
        elif(abs1 < abs2):
            print('Ближайшее к числу {} в списке: - это число {}'.format(x, number1)) 
        else:
            print('Ближайшее к числу {} в списке: - это число {}'.format(x, number2))
find_elem(list)