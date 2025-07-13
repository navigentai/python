# Type Conversion in Python

# Convert string to integer
number_str = "50"
number = int(number_str)

# Convert float to string
pi = 3.14159
pi_str = str(pi)

# Convert to boolean
print("bool(\"\"):", bool(""))     # False - empty string
print("bool(\"text\"):", bool("text")) # True - non-empty string

print("number + 10:", number + 10)  # Now we can add numbers
print("Pi as text:", pi_str)
print("Type of number:", type(number))
print("Type of pi_str:", type(pi_str))