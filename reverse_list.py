def reverse_slice(arr, start, end):
    left_part = arr[:start]
    middle_part = arr[start:end][::-1]
    right_part = arr[end:]

    return left_part + middle_part + right_part
