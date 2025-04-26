# sum_of_digits.py

# Function to find the sum of digits of a number
def sum_of_digits(n):
    total = 0  # Start with 0
    while n > 0:
        total += n % 10  # Add the last digit to total
        n = n // 10      # Remove the last digit
    return total  # Return the sum

# Example usage:
print(sum_of_digits(1234))  # Should print 10
