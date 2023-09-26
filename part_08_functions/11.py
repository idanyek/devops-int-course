def only_one_poitive(*numbers):
    for num in numbers:
        if num > 0:
            return True
    return False


print(only_one_poitive(1, 2))
print(only_one_poitive(-1, -2))
print(only_one_poitive(-1,0,-3,5,-3))
print(only_one_poitive())