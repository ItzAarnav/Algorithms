from palindrome_checker import check_palindrome


def test_true_normal_case():
    # Normal test case, with the output being True
    assert check_palindrome("dad") is True


def test_false_normal_case():
    # Normal test case, with the output being False
    assert check_palindrome("abcd") is False


def test_not_enough_char_string():
    # Leaving the string empty
    assert check_palindrome("") == "Not enough characters(char > 2)"

    # 2 character string
    assert check_palindrome("ab") == "Not enough characters(char > 2)"

    # 1 character string
    assert check_palindrome('a') == "Not enough characters(char > 2)"


def test_integers_in_argument():
    # Adding integers/floats in the parameter
    assert check_palindrome(12) == "Invalid input"



