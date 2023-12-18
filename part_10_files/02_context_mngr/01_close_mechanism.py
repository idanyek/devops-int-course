my_list = []

# for i in range(10000):
#     file = open("password.txt", "w")
#     my_list.append(file)
#     # print(my_list)
#     file.close()
#

for i in range(10000):
    with open("password.txt", "w") as file:
        my_list.append(file)
    print(i)
