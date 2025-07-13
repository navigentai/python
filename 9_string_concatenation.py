# String Concatenation in Python

# Concatenation means "combining strings"
# You use the '+' operator to join them

# Example 1: Simple string concatenation
print('hello' + ' Andrei')  # Output: hello Andrei

# Example 2: Using variables
first_name = 'Andrei'
greeting = 'Hello, '
message = greeting + first_name + '!'
print(message)  # Output: Hello, Andrei!

# Example 3: Adding spaces manually
word1 = 'Python'
word2 = 'Rocks'
sentence = word1 + ' ' + word2
print(sentence)  # Output: Python Rocks

# Example 4: Mixing with numbers (this will cause an error)
# Uncommenting below will raise a TypeError
# print("Age: " + 25)  # ❌ Cannot add string and integer directly

# Correct way: Convert number to string using str()
print("Age: " + str(25))  # ✅ Output: Age: 25