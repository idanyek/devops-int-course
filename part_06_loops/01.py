upper_number = int(input("enter a number at least 30 or higer: "))
for i in range(1,upper_number+1):
    print(i)
    if i % 4 == 0 and i % 7 == 0:
        print("Israel Forever")
    if i % 4 == 0:
        print("Israel")
    if i % 5 == 0:
        print("Forever")