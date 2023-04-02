# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из
# одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам



print('Введите стихотворение Винн-Пуха:')
str_ = input()
dict_puh_eng = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5, 'Y': 6, 'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'y': 6}
dict_puh_rus = {'А': 1, 'Е': 2, 'Ё': 3, 'И': 4, 'Й': 5, 'О': 6, 'У': 7, 'Ы': 8, 'Э': 9, 'Ю': 10, 'Я': 11,
                'а': 1, 'е': 2, 'ё': 3, 'и': 4, 'й': 5, 'о': 6, 'у': 7, 'ы': 8, 'э': 9, 'ю': 10, 'я': 11}


# Вариант решения задачи простым, более понятным способом, используя циклы.

some_list = str_.split(' ')
count = 0
vowel_count_list = []
for i in range(len(some_list)):
    temp = some_list[i]
    for i in temp:
        if i in dict_puh_eng or i in dict_puh_rus:
            count += 1
    vowel_count_list.append(count)
    count = 0
print('Решение №1 : ')
print(f'Список количества гласных букв в каждой фразе стихотворения - {vowel_count_list}')
vovel_count_set = set(vowel_count_list)
if len(vovel_count_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')


# вариант решения задачи используя функции высшего порядка

count_vovel_list = []
for i in range(len(some_list)):
    count_vovel_list.append(len(list(filter(lambda x: x in dict_puh_rus or x in dict_puh_eng, some_list[i]))))
print('Решение №2 : ')
print(f'Список количества гласных букв в каждой фразе стихотворения - {count_vovel_list}')
if len(set(count_vovel_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')