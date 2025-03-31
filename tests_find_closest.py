from find_closest import find_closest


def test_find_closest():
    assert find_closest([10, 2, 14, 4, 7], 6) == 7
    assert find_closest([1, 3, 5, 7, 9], 6) == 5
    assert find_closest([10, 20, 30], 25) == 20
    assert find_closest([10, 20, 30], 15) == 20
    assert find_closest([1], 5) == 1