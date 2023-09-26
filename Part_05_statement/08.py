num_01 = int(input("enter number 1: "))
num_02 = int(input("enter number 2: "))
num_03 = int(input("enter number 3: "))

if num_01 == num_02 and num_01 == num_03:
    print(3)
elif num_01 == num_02 or num_02 == num_03 or num_01 == num_03:
    print(2)
else:
    print(0)
