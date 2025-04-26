# factorial_loop.py

# Function to find factorial of a number using a loop
def factorial_loop(n):
    result = 1  # Start with 1 because factorial of 0 is 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply result by current number
    return result  # Return the factorial

# Example usage:
print(factorial_loop(5))  # Should print 120
