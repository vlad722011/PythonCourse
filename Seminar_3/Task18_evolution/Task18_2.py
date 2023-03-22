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
    Ai = int(input())
    list.append(Ai)
print('Итак, на вход мы имеем список:')
print(list)
list.sort()
print('Введите число "Х":')
x = int(input())
delta1 = delta2 = 0
first_left = first_right = 0
for j in range(len(list)):
    n = list[j] - x
    if (j != 0 and n >= 0):
        first_right = list[j]
        first_left = list[j-1]
        delta1 = first_right - x  
        delta2 = x - first_left 
        if (delta1 == delta2):
            print('Ближаишие к числу {} в списке: - это числа {} и {}'.format(x, first_left, first_right))
            break
        elif(delta1 < delta2):
            print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_right))
            break
        else:
            print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_left))
            break
    elif(j == 0 and n >= 0):
        first_right = list[0]
        print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_right))
        break
    elif(j == (len(list)-1) and n <= 0):
        first_left = list[j]
        print('Ближаишее к числу {} в списке: - это число {}'.format(x, first_left))
        break