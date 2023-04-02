# Ввод
# 3
# 9 28 21 23 12 41
# 6 21 18 26 41 18 23 53
# 18 4 25 31 15 20 31 1
# 2 13 10 28 12
# 10 31 23 13 121 17 9 18
# 31 9 3 10 121 4 14 21


print('Введите количество пар строк:')
n = int(input())
print('Введите строки, в которых числа разделены пробелами:')
#some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for i in range(2 * n)]
#print(some_list)
some_list = []
for _ in range(2 * n):
    temp_list = []
    for i in input().split():
        if i[-1] in('1', '3'):
            temp_list.append(i)
    some_list.append(temp_list)
#print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ')
