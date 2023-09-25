my_list = "Kuti"

for number in my_list:
    print(number)

for number in enumerate(my_list):
    print(number)

for index, number in enumerate(my_list):
    print(index, number)

for index, number in enumerate(my_list):
    print(f"{index+1}: {number} - completed")
