def reverse(text: str):
    return text[::-1]


def isPalindrome(text: str):
    if text == reverse(text):
        return f"the word {text} is a Palindrome"
    else:
        return f"the word {text} is NOT a Palindrome"


print(isPalindrome(input("Enter a word to check: ")))


