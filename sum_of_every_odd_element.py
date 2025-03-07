def sum_of_odd_elements(lst):
    """Finds the sum of every odd element in a list."""
    odd_elements = []

    for i in range(1, len(lst), 2):
        odd_elements.append(lst[i])

    total = 0
    for element in odd_elements:
        total += element

    return total

array = ["i", 0 , 0, 0, 0, 0, 1, 2]
print(sum_of_odd_elements(array))