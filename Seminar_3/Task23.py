# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает 
# количество элементов массива, больших предыдущего (элемента с предыдущим номером).

input_list = []
list_len = int(input("Введите количество элементов в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f"Введите число: ")))
    print(input_list)
    count = 0
    for i in range(list_len - 1):
        if input_list[i] < input_list[i + 1]:
            count += 1
            print(f"Количество элементов массива, больших предыдущего : {count}")