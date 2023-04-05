def edited(text: str):
    fio = input('Введите новое имя:')
    num = input('Введите новый номер телефона:')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(num) == 0:
        fio = text.split(' | ')[1]
    return f'{fio} | {num}'

a = ['Влад | +78982', 'Миха | 90890']
b = 'Влад | +78982'
#a[a.index(b)] = 'ВАся | 12345'
a[a.index(b)] = edited(b)
print(a)