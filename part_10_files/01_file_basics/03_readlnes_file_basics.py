my_file = open("file.txt")
# print(my_file.readlines())
# print(type(my_file.readlines()))

list_of_data = my_file.readlines()

for item in list_of_data:
    print(item,end="")

my_file.close()
