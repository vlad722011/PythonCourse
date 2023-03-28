import time
import random
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
input_list = []
for i in range(100000):
    number = random.randint(1, 8)
    s = generate_random_string(number)
    input_list.append(s)
input_list = list(set(input_list))
#print(input_list)

start_gpt = time.perf_counter()
groups = {}
# проходим по каждому слову
for word in input_list:
    # создаем ключ на основе отсортированных букв
    key = ''.join(sorted(word))
    # добавляем слово в список соответствующей группы
    groups.setdefault(key, []).append(word)
# выводим списки групп
print(list(groups.values()))
end_gpt = time.perf_counter()
time_gpt = end_gpt - start_gpt
print('Время выполнения gpt : - {}'.format(time_gpt))



start_my = time.perf_counter()
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
def f1(col):
    keys_list = list(col.keys())
    list_keys_values = []
    for i in keys_list:
        list_keys_values.append(temp_dictionary.get(i))
    return list_keys_values
def f2(col):
    list_sortvalue = []
    for i in range(len(list_value)):
        list_temp = list_value[i]
        list_temp.sort()
        list_sortvalue.append(list_temp)
        list_temp = []
    return list_sortvalue
def f3(col):
    dictionary_temp2 = {}
    for i in range(len(input_list)):
        dictionary_temp2[input_list[i]] = list_sort_value[i]
    return dictionary_temp2
def f4(col):
    list_result = []
    for i in temp_dictionary2:
        value_i = temp_dictionary2.get(i)
        keys_for_value = {i for i in temp_dictionary2 if temp_dictionary2[i] == value_i}
        keys_for_value = list(keys_for_value)
        list_result.append(keys_for_value)
    return list_result
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
result = f5(temp_result)
print(result)
end_my = time.perf_counter()
time_my = end_my - start_my
print('Время выполнения my: - {}'.format(time_my))
print('Кто быстрее  и во сколько раз (time_my / time_gpt): - {}'.format(time_my / time_gpt))