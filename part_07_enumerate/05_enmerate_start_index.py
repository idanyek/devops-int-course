my_list = [10, 20, 30, 40, 50]
for number in my_list:
    print(number)

for number in enumerate(my_list,start=1):
    print(number)

for index, number in enumerate(my_list,start=1):
    print(index, number)

for index, number in enumerate(my_list, start=1):
    print(f"{index}: {number} - completed")
