

def fibonacci(n):
    # Base cases: F(0) = 0 and F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursively sum the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usages
print(fibonacci(5))
print(fibonacci(10))
