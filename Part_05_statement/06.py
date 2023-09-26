num_01 = int(input("enter number 1: "))
num_02 = int(input("enter number 2: "))

if num_01 >= num_02:
    maximum = num_01
    minimum = num_02
else:
    maximum = num_02
    minimum = num_01

print(f"{minimum} {maximum}")
print(f"{maximum=}")
print(f"{minimum=}")