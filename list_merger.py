
def sorted_list(numbers, order):
    """
    Sorts the array in ascending or descending order based on the 'order' parameter.

    Parameters:
    numbers (list): The list of numbers to be sorted.
    order (bool): If True, sort in ascending order; if False, sort in descending order.

    Returns:
    list: The sorted list.
    """
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if (order and numbers[i] > numbers[j]) or (not order and numbers[i] < numbers[j]):
                # Swap elements
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


def list_merge(list1, list2, sorts):

    """Merge 2 lists without having to edit any of the original lists
    Change the 3rd parameter to True if you want to sort them as well.
    If not, be sure to set it to False"""

    new_list = list1

    for i in list2:
        new_list.append(i)

    if sorts:
        sorted_list(new_list, True)
    else:
        sorts = False
    return new_list


array = [-3, 0, 5]
array2 = [-2, 1, 4]


print(list_merge(array, array2, True))


