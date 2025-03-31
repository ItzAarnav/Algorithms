def find_closest(arr, target):
    closest = arr[0]
    min_diff = abs(arr[0] - target)

    for num in arr:
        diff = abs(num - target)
        if diff < min_diff:
            min_diff = diff
            closest = num

    return closest


# Test the function
arr = [10, 2, 14, 4, 7]
target = 6
print(find_closest(arr, target))
