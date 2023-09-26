sentence = input("enter your word: ")

if sentence[-1] == "?":
    type_of_sentence = "Question"
else:
    type_of_sentence = "Regular"

print(f"Your {sentence=} is: {type_of_sentence}")

