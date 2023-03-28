# Задача №4. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.

def is_number_simple(number):
    if number != 2 and number % 2 == 0:
        return False
    for i in range(3, number // 2 + 1, 2):
        if number % i == 0:
            return False
    return True
input_number = int(input("Введите число, для проверки является ли оно простым: "))
print(is_number_simple(input_number))
