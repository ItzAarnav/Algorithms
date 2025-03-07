
def sort_letters(input_string):
    letters = [char.lower() for char in input_string if char.isalpha()]

    n = len(letters)
    for i in range(n):
        for j in range(0, n - 1):
            if letters[j] > letters[j + 1]:
                letters[j], letters[j + 1] = letters[j + 1], letters[j]

    return ''.join(letters)


string = "ilya"
sorted_string = sort_letters(string)
print(sorted_string)
