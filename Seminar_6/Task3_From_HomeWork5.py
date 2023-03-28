# Задача. На входе дан некоторый список слов: - Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Необходимо на выходе получить список списков, в котором слова будут сгруппированы по "общим буквам"
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

def group_letter(input_list):
    word_dict = {}
    for word in input_list:
        if (frozenset(word), len(word)) not in word_dict:
            word_dict[(frozenset(word), len(word))] = [word]
        else:
            word_dict[(frozenset(word), len(word))].append(word)
    res_list = []
    for value in word_dict.values():
        res_list.append(value)
    return res_list

print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat", 'batt', 'b', 'cadfsdf']))

