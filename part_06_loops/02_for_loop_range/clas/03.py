number1 = int(input("enter a number1: "))
number2 = int(input("enter a number2: "))

for i in range(number1,number2+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)