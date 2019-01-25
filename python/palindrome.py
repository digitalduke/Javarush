# py3
from string import punctuation

def clear_string(text):
    cleared_string = ""

    for c in something[::]:
        if not c in punctuation:
            cleared_string += c

    return cleared_string.replace(" ", "").lower()

def is_palindrome(text):
    return clear_string(text) == clear_string(text[::-1])

something = input("Enter phrase: ")

if is_palindrome(something):
    print("This is palindrome")
else:
    print("No, it's not a palindrome")
