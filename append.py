# My append function. Works like the normal one

def my_append(array, element):
    """Appends an element at the end of a list"""
    new_array = [0 for _ in range(len(array) + 1)]
    # print(new_array)
    for i in range(0, len(array)):
        new_array[i] = array[i]
    new_array[len(array)] = element
    return new_array
