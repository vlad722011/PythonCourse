import random
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
    return rand_string
input_list = []
for i in range(50000):
    number = random.randint(1, 15)
    s = generate_random_string(number)
    input_list.append(s)
input_list = list(set(input_list))
print(input_list)
