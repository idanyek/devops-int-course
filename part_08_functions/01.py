def get_text_lengh(text: str = "Hello"):
    return len(text)


def get_text_list(texts: list):
    count = 0
    for text in texts:
        count += get_text_lengh(text)
    return count



print(get_text_lengh("Hello World"))
print(get_text_list(["hello", "world", "my"]))
