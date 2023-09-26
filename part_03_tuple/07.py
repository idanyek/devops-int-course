tuple_1 = 11, [22, 33], 44, 55
list_tuple_1 = list(tuple_1)
list_tuple_1[1][0] = 222
tuple_1 = tuple(list_tuple_1)
print(f"{tuple_1=}")