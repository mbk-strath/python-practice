# factorial_recursive.py

# Function to find factorial of a number using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive call

# Example usage:
print(factorial_recursive(5))  # Should print 120
