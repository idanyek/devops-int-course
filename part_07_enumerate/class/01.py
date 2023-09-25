words = ["java", "python", "javascript", "php", "typescript"]

print(list(enumerate(words, start=1)))
words2 = [(word, index) for index, word in list(enumerate(words, start=1))]
print(words2)

words_list = []
for index, word in enumerate(words, start=1):
    words_list.append((word, index))
print(words_list)