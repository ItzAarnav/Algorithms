def remove_duplicates(lst):

    """Creates a new list with unique items, each not duplicated as it was in the old list.
    Just insert a list and done! Your list will be returned"""
    unique_elements = []

    for element in lst:
        is_duplicate = False
        for unique in unique_elements:
            if element == unique:
                is_duplicate = True
                break

        if not is_duplicate:
            unique_elements.append(element)

    return unique_elements


array = [1, 1, 1, 2, 2, 3, 3]
print(remove_duplicates(array))