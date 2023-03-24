# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему
# добавляется количество повторений.


#input_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
input_str = 'AAAABBBCCXYZDDDDEEEFFGGGKLRDYUIKKKFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
print('Входящая строка:- {}'.format(input_str))

# В первой функции из входящей строки получим временную строку, в которой символы будут идти без повторов.
def f(col):
    output_str_temp = input_str[0]
    index_output_str_temp = 0
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == output_str_temp[index_output_str_temp]:
            count += 1
        else:
            index_output_str_temp += 1
            output_str_temp += input_str[i]
    return output_str_temp

# Функция, которая вернет список чисел. Числа списка укажут количество повторов символов входящей строки.
def f1(col):
    char_count = []
    count = 0
    count1 = 0
    for i in range(len(str_temp1)):
        char = str_temp1[i]
        for j in range(count1, len(input_str)):
            char2 = input_str[j]
            if char2 == char:
                count += 1
                count1 += 1
            else:
                char_count.append(count)
                count = 0
                break
    char_count.append(count)
    char_count = list(map(str, char_count))
    return char_count

# Функция вернет итоговую строку
def f2(col):
    output_str_end = ''
    for i in range(len(str_temp1)):
        for j in range(len(chars_counter)):
            if i == j:
                s1 = str_temp1[i]
                output_str_end += s1
                s2 = chars_counter[j]
                if (s2 != '1'):
                    output_str_end += s2
    return output_str_end

str_temp1 = f(input_str)
#print('Результат работы первой функции: - {}'.format(str_temp1))

chars_counter = f1(input_str)
#print('Результат работы второй функции: - {}'.format(chars_counter))

str_result = f2(str_temp1)
print('Выходящая строка: - {}'.format(str_result))
