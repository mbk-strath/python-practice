# even_or_odd.py

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"  # Number is divisible by 2
    else:
        return "Odd"   # Number is not divisible by 2

# Example usage:
print(check_even_odd(7))  # Should print "Odd"
