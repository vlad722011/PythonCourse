# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему
# добавляется количество повторений.


def rle(some_str):
    res_list = []
    some_str += ' '
    temp_letter = some_str[0]
    count_letter = 1
    for ind in range(1, len(some_str)):
        if some_str[ind] == temp_letter:
            count_letter += 1
        else:
            if count_letter == 1:
                res_list.append(f'{temp_letter}')
                count_letter = 1
                temp_letter = some_str[ind]
            else:
                res_list.append(f'{temp_letter}{count_letter}')
                count_letter = 1
                temp_letter = some_str[ind]
    print(res_list)
    print(*res_list, sep='')


rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
