def cyclic_shift_right(arr, n):
    if not arr:
        return arr

    n = n % len(arr)  # Handle cases where n > len(arr)
    result = [0] * len(arr)

    for i in range(len(arr)):
        new_position = (i + n) % len(arr)
        result[new_position] = arr[i]

    return result


# Example usage
array = [1, 2, 3, 4, 5]
n = 2
result = cyclic_shift_right(array, n)
print(f"Array after {n} right shifts: {result}")