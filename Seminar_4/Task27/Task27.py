# 27. Пользователь вводит текст(строка). Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов или символами
# конца строки. Определите, сколько различных слов содержится в этом тексте.


# print('Введите строку:')
# s = input()
s = 'Здравствуйте, я ваша тетя Мотя. Вам привет от Дяди Федора! Знаете такого? Томск. Я! тетя, Мотя, Федор!'
str_list = list(s)
char_space = ' '
char_dot = '.'
char_comma = ','
char_exclamation_point = '!'
char_question = '?'
word = ""
word_list = []
for i in range(len(s)):
    char = s[i]
    if ((char != char_space) and (char != char_dot) and (char != char_comma) and (char != char_exclamation_point) and (char != char_question)):
        word += char
    elif ((char == char_space) or (char != char_dot) or (char != char_comma) or (char == char_exclamation_point) or (char == char_question)):
        word_list.append(word)
        word = ""    
word_list.append(word)
word_list_end = []
for i in range (len(word_list)):
    word_i = word_list[i]
    if (word_i != ''):
        word_list_end.append(word_i)
print(word_list_end)
word_list_end = set(word_list_end)
number = len(word_list_end)
print(number)


