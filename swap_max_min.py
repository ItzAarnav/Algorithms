def swap_min_max(lst):

    if not lst:
        return lst

    min_index = 0
    max_index = 0

    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
        if lst[i] > lst[max_index]:
            max_index = i

    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

    return lst

array = [42, 8 , 45, 22, 7]
print(swap_min_max(array))