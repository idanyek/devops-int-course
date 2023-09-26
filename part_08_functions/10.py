def multiply(*numbers: int):
    res = 1
    for num in numbers:
        res = res * num
    return res


print(multiply(1,2,3))
print(multiply(1,3))
print(multiply(2))
print(multiply())