def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    with open('Phonebook.txt', 'a', encoding='utf-8') as f:
        fio = input("Введите ФИО: ")
        tel_number = int(input('Введите номер телефона: '))
        f.write('ФИО = {} | Номер телефона = {}\n'.format(fio,tel_number))

def find_data() -> None:
    '''Ищет информацию в справочнике'''
    data_to_find = input("Введите данные для поиска: ")

    with open('Phonebook.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print("Результаты поиска: ")
    print (search(tel_book, data_to_find))


def search(book : str, info: str):
    '''Находит в строке записи информацию по определенному критерию'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])
    # return [post for post in book if info in post]
