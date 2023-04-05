import functions

while True:
    print('1.вывод, 2. добавление, 3. поиск')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    else:
        break