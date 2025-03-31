from find_missing_number import find_missing_number


# Test cases for find_missing_number
def test_find_missing_number():
    assert find_missing_number([1, 2, 4, 5, 6]) == 3
    assert find_missing_number([1, 3, 4, 5, 6]) == 2
    assert find_missing_number([2, 3, 4, 5, 6]) == 1
    assert find_missing_number([1]) == 2
    assert find_missing_number([2]) == 1