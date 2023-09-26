word_1 = input("enter word 1: ")
word_2 = input("enter word 2: ")

if word_1[::-1] == word_2:
    print("YES")
else:
    print("NO")