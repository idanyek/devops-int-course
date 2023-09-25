number1 = int(input("enter a number1: "))
number2 = int(input("enter a number2: "))

for i in range(number1,number2+1):
    print(f"Number {i}; power of 2 = {i**2}; power of 3 = {i**3}")