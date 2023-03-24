# Задача. На входе дан некоторый список слов: - Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Необходимо на выходе получить список списков, в котором слова будут сгруппированы по "общим буквам"
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

import time



#input_list = list(set(["мир", "пир", "рим", "пар", "кот", "ток", "снег", "солнце", "питон", "лоск", "скол", "сколько",
# "мир", "пир", "рим", "пар", "кот", "ток", "eat", "tea", "tan", "ate", "nat", "bat",'саша', 'придавая', 'ему',
# 'хохоча', 'он', 'ниткин', 'помоев', 'шестикрылов', 'гамлет', 'он', 'что', 'он', 'приказчик', 'генерал', 'на', 'что',
# 'все', 'он', 'доктор', 'он', 'он', 'он', 'все', 'пробкин', 'помощник', 'ей', 'мамаше', 'вы', 'пять', 'он', 'человек',
# 'он', 'провизор', 'он', 'он', 'он', 'этого', 'поручик', 'кнапс', 'он', 'кнапс', 'вы', 'ершаков', 'он', 'мрачно', 'он',
# 'мне', 'надоест', 'мне', 'узелков', 'узелков', 'узелков', 'шапкин', 'лакей', 'что', 'ну', 'он', 'нельзя', 'ну', 'сын',
# 'он', 'старик', 'вам', 'скажи', 'он', 'он', 'фон', 'ну', 'семечкин', 'сладким', 'вам', 'николай', 'он', 'клочков',
# 'художник', 'медик', 'ей', 'медик', 'странная', 'он', 'но']))


#input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
#input_list = ["мир", "пир", "рим", "пар", "кот", "ток"]

input_list = ["мир", "пир", "рим", "пар", "кот", "ток", "снег", "солнце", "питон", "лоск", "скол", "сколько"]
print('Входящий список:- {}'.format(input_list))

start = time.perf_counter()
# Функция, результатом работы которой будет полученный словарь, в котором каждому слову-ключу будет соответствовать
# список-значение состоящий из букв слова
def f(col):
    dictionary_temp = {}
    for i in range(len(input_list)):
        word = input_list[i]
        temp_list = []
        for j in range(len(word)):
            char = word[j]
            temp_list.append(char)
            dictionary_temp[word] = (temp_list)
    return dictionary_temp

# Функция результатом работы которой будет полученный список, элементами которого будут списки всех значений словаря
# в нашем случае получим список из значений словаря полученного ранее
def f1(col):
    keys_list = list(col.keys())
    list_keys_values = []
    for i in keys_list:
        list_keys_values.append(temp_dictionary.get(i))
    return list_keys_values


# Функция, в результате работы которой списки значений будут отсортированы по алфавиту, чтобы далее, мы могли сравнить
# списки значения для разных ключей, и тем самым понять, как сгруппировать слова входящего списка
def f2(col):
    list_sortvalue = []
    for i in range(len(list_value)):
        list_temp = list_value[i]
        list_temp.sort()
        list_sortvalue.append(list_temp)
        list_temp = []
    return list_sortvalue


# Функция, результатом работы которой получим словарь где каждому слову-ключу входящего списка, будет соответствовать
# список-значение состоящий из букв слова, но списки занчения будут отсортированы по алфавиту
def f3(col):
    dictionary_temp2 = {}
    for i in range(len(input_list)):
        dictionary_temp2[input_list[i]] = list_sort_value[i]
    return dictionary_temp2


# Функция, результат работы которой - промежуточный список из из списков сгруппированным по "общим буквам" словам.
# Полученный список промежуточный, содержит повторы...
def f4 (col):
    list_result = []
    for i in temp_dictionary2:
        value_i = temp_dictionary2.get(i)
        keys_for_value = {i for i in temp_dictionary2 if temp_dictionary2[i] == value_i}
        keys_for_value = list(keys_for_value)
        list_result.append(keys_for_value)
    return list_result


# Собственно функция, в которой из просежуточного списка получаем итоговый - содержащий только уникальные элементы.
# Это и будет итоговый список, который требовалось получить в задаче.
def f5(col):
    result = []
    for i in range(len(temp_result)):
        element = temp_result[i]
        if element in result:
            i = i + 1
        else:
            result.append(element)
    return result

temp_dictionary = f(input_list)
list_value = f1(temp_dictionary)
list_sort_value = f2(list_value)
temp_dictionary2 = f3(list_sort_value)
temp_result = f4(temp_dictionary2)

# Получаем итоговый список, со сгруппированными по "общим буквам" словам, и выводим его на печать
result = f5(temp_result)
print('Список со сгруппированными по "общим буквам" словам: - {}'.format(result))

end = time.perf_counter()

runtime  = end - start
print('Время выполнения программы: - {}'.format(runtime))

