num1 = int(input("input number 1: "))
num2 = int(input("input number 2: "))
num3 = int(input("input number 3: "))

print(max(num1 + num2 * num3, num1 * (num2 + num3), num1 * num2 * num3, (num1 + num2) * 3))
