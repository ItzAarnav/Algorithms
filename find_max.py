# Change array for test

array = [4, 2, 181, 23]


def find_max(numbers):
    greatest_number = 0
    previous_number = 0

    for n in numbers:
        if n > greatest_number:
            greatest_number = n
        elif greatest_number < n:
            previous_number = n
    return greatest_number


print(find_max(array))
