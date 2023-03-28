import time
import random
some_list = [random.randint(1, 1000000) for _ in range(1000000)]
start = time.perf_counter()
print(100234 in some_list)
end = time.perf_counter()
first_time = end - start
some_set = set(some_list)
start = time.perf_counter()
print(40 in some_set)
end = time.perf_counter()
second_time = end - start
print(first_time / second_time)







