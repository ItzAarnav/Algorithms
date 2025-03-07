def my_insert(array, element, index):
    new_array = [0 for _ in range(len(array) + 1)]
    for i in range(index):
        new_array[i] = array[i]
    new_array[index] = element
    for i in range(index, len(array)):
        new_array[i + 1] = array[i]

    return new_array
