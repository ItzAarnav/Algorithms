"""
def check_palindrome(char: str):

    Check if a set of characters are a palindrome.

    Parameters:
    char(str): The string that is getting checked

    Returns:
    is_palindrome(bool): True if it is a correct palindrome, False if not.


    try:
        is_palindrome = False
        if len(char) > 2:
            split = []

            str(split)
            for i in char:
                split.append(i)

            new_char = split[::-1]

            if new_char == split:
                is_palindrome = True
                return is_palindrome
            else:
                return is_palindrome
        else:
            return "Not enough characters(char > 2)"
    except TypeError:
        return "Invalid input"


# Test Case
characters = "2121212"
print(check_palindrome(characters))
"""


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: Fals
