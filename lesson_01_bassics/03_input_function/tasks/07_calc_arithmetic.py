num1, num2, num3, num4 = map(int,input("please enter 4 numbers, sepereted by space: ").split())
print((num1+num2+num3+num4)/4)

#or

print((sum(list(map(int,input("please enter 4 numbers, sepereted by space: ").split()))))/4)

#or
list_of_items = list(map(int,input("please enter numbers, sepereted by space: ").split()))
print(sum(list_of_items) / len(list_of_items))