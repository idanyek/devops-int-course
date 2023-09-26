def count_args(*numbers):
    return len(numbers)


print(count_args(1, 2, 3))
print(count_args(1, 2))
print(count_args(1))
print(count_args())