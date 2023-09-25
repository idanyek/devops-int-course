my_list = [10, 20, 30, 40, 50]

for number in my_list:
    print(number)

for number in enumerate(my_list):
    print(number)

for index, number in enumerate(my_list):
    print(index, number)

for index, number in enumerate(my_list):
    print(f"{index+1}: {number} - completed")
