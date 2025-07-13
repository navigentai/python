# Functions are standalone, while methods belong to objects

# Function example
print(len("hello"))  # len() is a built-in function

# Method example
text = "hello"
print(text.upper())  # upper() is a method called on the string object

# More examples
numbers = [1, 2, 3]
print(len(numbers))      # Function: gets length of list
numbers.append(4)        # Method: adds 4 to the list
print("Updated list:", numbers)

# You can call many methods on objects
print(text.replace("h", "H"))  # Method: replaces