def find_missing_number(arr):
    n = len(arr)
    # did a BIT of research to get this below
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum

    return missing_number


# Test the function
arr = [1, 2, 4, 5, 6]
print(find_missing_number(arr))  # Output: 3
