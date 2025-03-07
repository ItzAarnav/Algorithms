import find_max  # A custom library


def find_second_largest_element(sequence):
    """Finds the second-largest element in a list. INPUT: An array
    OUTPUT: second-largest element"""
    new_list = [i for i in sequence]  # List comprehension to create separate child list

    greatest_element = find_max.find_max(new_list)  # Uses functions from library

    for i in new_list:
        if i == greatest_element:
            new_list.remove(greatest_element)
    second_greatest = find_max.find_max(new_list)

    return second_greatest


# Running Scripts
array = [1, 4, 2, 3, 5]
print(find_second_largest_element(array))
