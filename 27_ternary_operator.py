# Ternary Operator in Python (shorthand for simple if-else logic)

age = 17
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Another example: check if a number is even or odd
number = 8
parity = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {parity}")

# You can use ternary operator for quick assignments
temperature = 25
weather = "Hot" if temperature > 30 else "Comfortable"
print("Weather:", weather)