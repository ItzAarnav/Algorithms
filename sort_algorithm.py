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


# Example usage
numbers_list = [1, 5, 2]
print(sorted_list(numbers_list, True))  # Output: [1, 2, 5]
print(sorted_list(numbers_list, False))  # Output: [5, 2, 1]
