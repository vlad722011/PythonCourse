# 21. Напишите программу для печати всех уникальных значений в словаре.

input_dict = {}
input_dict_len = int(input("Введите количество пар: "))
for _ in range(input_dict_len):
    input_key = input("Введите ключ: ")
    input_value = input("Введите значение: ")
    input_dict[input_key] = input_value
    print(set(input_dict.values()))