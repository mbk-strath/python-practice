# reverse_string.py

# Function to reverse a string without using [::-1]
def reverse_string(s):
    reversed_str = ""  # Start with an empty string
    for char in s:
        reversed_str = char + reversed_str  # Add each character to the front
    return reversed_str  # Return the reversed string

# Example usage:
print(reverse_string("hello"))  # Should print "olleh"
