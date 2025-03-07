def my_delete(array, index):
    new_array = [0 for _ in range(len(array) - 1)]

    for i in range(index):
        new_array[i] = array[i]

    for i in range(index + 1, len(array)):
        new_array[i - 1] = array[i]

    return new_array
