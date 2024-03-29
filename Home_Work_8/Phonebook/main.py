# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных

# Логика алгоритма для изменения:
# Прочитать информацию из файла, сохранить ее в некоторую переменную
# Внести нужные правки в этой информации (для этого нужно вызвать поиск, чтобы понять, что конкретно меняем)
# Перезаписать файл, используя мод 'w'
# P.S. Для уточнения поиска редактируемого элемента можно воспользоваться функцией enumerate.
# Для нахождения индекса вхождения в массиве можно использовать .index(<вхождение>)

import functions

while True:
    print('1.вывод, 2. добавление, 3. поиск, 4. редактирование данных, 5. удаление данных')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode ==4 :
        functions.change_data()
    elif mode ==5 :
        functions.delete_data()
    else:
        break
