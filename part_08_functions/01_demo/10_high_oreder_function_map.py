def multiple(num: int,num2:int = 3):
    return num * num2

array = [10,20,30,40,50]

after_map = map(lambda x: x * 2, array)

print(after_map)
print(type(after_map))

print(list(after_map))

after_map = map(multiple, array)

print(after_map)
print(type(after_map))

print(list(after_map))