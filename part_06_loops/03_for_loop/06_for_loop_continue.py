
my_list = list(range(0,200,3))
for x in my_list:
    if x % 2 != 0:
        continue
    print(x)