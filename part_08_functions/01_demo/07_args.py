def my_function(*lang):
    if len(lang) >= 3:
        print(f"My favorite lang is: {lang[2]}")


def itrate_lang(*lang):
    print(lang)
    print(type(lang))
    for i in lang:
        print(i, end=" | ")


my_function("python", "php", "java")
itrate_lang("python", "php", "java")
