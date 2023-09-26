def my_function(foods):
    print(foods)
    print(type(foods))
    for food in foods:
        print(food, end=" | ")
    print("")


fruits = ["apple", "banana", "char"]
my_function(fruits)
fruits = ("apple", "banana", "char")
my_function(fruits)
fruits = "apple"
my_function(fruits)
fruits = 546620807
my_function(fruits)

