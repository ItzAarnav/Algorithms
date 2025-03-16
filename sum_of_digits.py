def sum_of_digits(n):
    # Base case: when n is a single digit
    if n == 0:
        return 0
    else:
        # Recursively sum the digits by taking the last digit (n % 10)
        return n % 10 + sum_of_digits(n // 10)

# Example usages
print(sum_of_digits(123))  # Output: 6 (1+2+3)
print(sum_of_digits(405))  # Output: 9 (4+0+5)
