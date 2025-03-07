"""
A simple algorithm to find the place of a specific item in an array, using Binary Search.
INPUT: Takes in a "sequence," which is the list, and takes in an "item," which is the item searched throughout the
entire list.
OUTPUT: The code will have two different outputs:
    1[If the item is found]: Will return the index of your item.
    2[If item not found throughout array]: Will return None

Remember, use this in a list sorted by ascending order. If not, the algorith will automatically sort it.

BY AARNAV

"""


def binary_search(sequence, item):
    """Find the index and place of a specific item in a list"""
    sorted(sequence)
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None
