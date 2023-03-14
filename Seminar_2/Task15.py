# Задача 15. Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много, и он не знает, как же
# выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30.


print('Введите целое число, колличество рассматриваемых арбузов:')
n = int(input())
for i in range(n):
    print('Введите вес арбуза:')
    weight_arbuz = (int)(input())
    while (weight_arbuz <= 0 or weight_arbuz > 30):
        print('Введите корректный вес арбуза:')
        weight_arbuz = (int)(input())
    if (i == 0):        
        weight_arbuz_max = weight_arbuz_min = weight_arbuz
    if (weight_arbuz < weight_arbuz_min):
        weight_arbuz_min = weight_arbuz
    elif (weight_arbuz > weight_arbuz_max):
        weight_arbuz_max = weight_arbuz
print('Арбуз для себя: {}'.format(weight_arbuz_max))
print('Арбуз для тещи: {}'.format(weight_arbuz_min))
