# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных

# Логика алгоритма для изменения:
# Прочитать информацию из файла, сохранить ее в некоторую переменную
# Внести нужные правки в этой информации (для этого нужно вызвать поиск, чтобы понять, что конкретно меняем)
# Перезаписать файл, используя мод 'w'
# P.S. Для уточнения поиска редактируемого элемента можно воспользоваться функцией enumerate.
# Для нахождения индекса вхождения в массиве можно использовать .index(<вхождение>)


def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    with open('Phonebook.txt', 'a', encoding='utf-8') as f:
        fio = input("Введите ФИО: ")
        tel_number = int(input('Введите номер телефона: '))
        f.write('\n{} | {}'.format(fio, tel_number))
    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        data_file = f.read()
        data_list = data_file.split('\n')
        for i in data_list:
            if i == '':
                data_list.remove(i)
    with open('Phonebook.txt', 'w', encoding='utf-8') as f:
        for i in range(len(data_list)):
            if i == 0:
                f.write(data_list[i])
            else:
                f.write('\n')
                f.write(data_list[i])


def find_data() -> None:
    '''Ищет информацию в справочнике'''
    data_to_find = input("Введите данные для поиска: ")
    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print("Результаты поиска: ")
    print(search(tel_book, data_to_find))


def search(book: str, info: str):
    '''Находит в строке записи информацию по определенному критерию'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def change_data() -> None:
    '''Редактирует данные в файле'''
    data_to_change = input('Введите данные, которые необходимо обновить:')
    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        data_file = f.read()
        data_list = data_file.split('\n')
        print(f'Список абонентов в справочнике: {data_list}')
        temp_data_list = search(data_file, data_to_change).split('\n')
        if len(temp_data_list) != 1:
            print(f'Список абонентов, которые соответствуют данным, подлежащим изменению: {temp_data_list}')
            for i, val in enumerate(temp_data_list, start=1):
                print(f'№ {i} => {val}')
            print('Уточните абонента, данные которого необходимо отредактировать, введите номер: ')
            n = int(input())
            abonent = temp_data_list[n - 1]
            print(f'Будут редактироваться данные абонента {abonent}')
        else:
            print(f'Абонент, данные которого соответствуют данным, подлежащим изменению: {temp_data_list}')
            abonent = temp_data_list[0]
        print('Введите новые данные ниже: ')
        new_fio = input('Введите новое имя:')
        new_tel = input('Введите новый номер телефона:')
        new_data_str = new_fio + ' | ' + new_tel
        data_list[data_list.index(abonent)] = edited(new_data_str, new_fio, new_tel)
        print(f'Изменненый список абонентов справочника: {data_list}')
        with open('Phonebook.txt', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if i == 0:
                    f.write(data_list[i])
                else:
                    f.write('\n')
                    f.write(data_list[i])


def edited(text: str, fio: str, tel: str):
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(tel) == 0:
        fio = text.split(' | ')[1]
    return f'{fio} | {tel}'


def delete_data() -> None:
    '''Удаляет данные из файла'''
    data_to_delete = input('Введите данные, которые необходимо удалить:')
    abonent = ''
    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        data_file = f.read()
        data_list = data_file.split('\n')
        print(f'Список абонентов в справочнике: {data_list}')
        temp_data_list = search(data_file, data_to_delete).split('\n')
        if len(temp_data_list) != 1:
            print(f'Список абонентов, которые соответствуют данным, подлежащим удалению: {temp_data_list}')
            for i, val in enumerate(temp_data_list, start=1):
                print(f'№ {i} => {val}')
            print('Уточните абонента, данные о котором необходимо удалить, введите номер: ')
            n = int(input())
            abonent = temp_data_list[n - 1]
            print(abonent)
            print(f'Данные об абоненте {abonent}, удалены успешно')
        elif len(temp_data_list) == 1:
            print(f'Будут удалены данные об абоненте: {temp_data_list[0]}')
            abonent = temp_data_list[0]
            print(f'Данные об абоненте {abonent}, удалены успешно')
        for i in data_list:
            if i == abonent:
                data_list.remove(i)
        with open('Phonebook.txt', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if i == 0:
                    f.write(data_list[i])
                else:
                    f.write('\n')
                    f.write(data_list[i])



while True:
    print('1.вывод, 2. добавление, 3. поиск, 4. редактирование данных, 5. удаление данных')
    mode = int(input())
    if mode == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode ==4 :
        change_data()
    elif mode ==5 :
        delete_data()
    else:
        break

