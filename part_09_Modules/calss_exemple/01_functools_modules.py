from functools import reduce

my_list = list(range(2, 11))

print(reduce(lambda x, y: x * y, my_list))


