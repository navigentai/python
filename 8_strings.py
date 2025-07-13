# Strings are used to store text

greeting = "Hello"
name = "Jamie"
full_message = greeting + ", " + name + "!"  # Combine strings with +

print(full_message)

# You can also use formatted strings for better readability
formatted_message = f"{greeting}, {name}!"
print(formatted_message)

# Check types
print("Type of greeting:", type(greeting))
print("Type of name:", type(name))
print("Type of full_message:", type(full_message))
# Example of string methods
print("Uppercase greeting:", greeting.upper())  # Convert to uppercase
print("Lowercase name:", name.lower())          # Convert to lowercase
print("Length of full_message:", len(full_message))  # Get length of string 