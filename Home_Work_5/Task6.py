# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему
# добавляется количество повторений.

input_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
print('Входящая строка:- {}'.format(input_str))

def f(col):
    output_str = ''
    count = 0
    count1 = 0
    for i in col:
        if count1 != len(col):
            char = col[count1]
        else:
            break
        for j in range(count1, len(col)):
            char2 = input_str[j]
            if char2 == char:
                count += 1
                count1 += 1
            else:
                output_str += char
                count = str(count)
                if count != '1':
                    output_str += count
                count = 0
                break
    output_str += col[-1]
    count = str(count)
    output_str += count
    return output_str
str_result = f(input_str)
print('Выходящая строка: - {}'.format(str_result))
