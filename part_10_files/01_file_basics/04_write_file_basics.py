# W - write, w+ - write + read
# a - append, a+ - append and read
my_file1 = open("file.txt")

my_file = open("file2.txt", "w")
my_file.write("111\n")
my_file.writelines(my_file1.readlines())
