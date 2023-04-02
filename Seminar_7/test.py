# Ввод
# 3
# 9 28 21 23 12 41
# 6 21 18 26 41 18 23 53
# 18 4 25 31 15 20 31 1
# 2 13 10 28 12
# 10 31 23 13 121 17 9 18
# 31 9 3 10 121 4 14 21



input_str_list = {}
input_len_str_list = int(input("Введите количество пар строк: "))
for i in range(input_len_str_list):
    input_str_list[i] = []
    input_str_list[i].append(list(map(lambda x: int(x), input("Введите числа разделённые пробелами: ").split())))
    input_str_list[i].append(list(map(lambda x: int(x), input("Введите числа разделённые пробелами: ").split())))
    result = []
    for couple in input_str_list:
        for i in range(2):
            result.append(list(set(list(filter(lambda x: x % 10 == 1 or x % 10 == 3, input_str_list[couple][i])))))
print(result)
