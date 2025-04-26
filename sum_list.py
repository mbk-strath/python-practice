# sum_list.py

# Function to sum all elements in a list
def sum_list(numbers):
    total = 0  # Start with a total of 0
    for num in numbers:
        total += num  # Add each number to total
    return total  # Return the final sum

# Example usage:
print(sum_list([1, 2, 3, 4, 5]))  # Should print 15
