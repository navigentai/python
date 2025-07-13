# Fundamental Number Types and Arithmetic Operations in Python

# int – Whole numbers (e.g., 1, 0, -5)
# float – Numbers with a decimal point (e.g., 3.14, 0.5)

# Define numbers
a = 10       # int
b = 3        # int
c = 2.5      # float

print("--- TYPES ---")
print("Type of a:", type(a))
print("Type of c:", type(c))
print("Type of a / b:", type(a / b))  # Division always returns float

print("\n--- ARITHMETIC OPERATIONS ---")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponentiation (b ** 2):", b ** 2)

print("\n--- REAL-WORLD EXAMPLE ---")
# Real-world example: calculating the total cost of items including tax
price_per_item = 49.99
quantity = 3
tax_rate = 0.07

subtotal = price_per_item * quantity
total = subtotal * (1 + tax_rate)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Total with Tax: ${total:.2f}")

print("\n--- EXERCISES ---")
# Area of a rectangle
length = 12.5
width = 4.3
area = length * width
print("Area of rectangle:", area)

# Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
# Calculate the square of a number
num = 8
square = num ** 2
print("Square of", num, "is", square)
# Calculate the average of three numbers
num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3) / 3
print("Average of", num1, num2, "and", num3, "is", average)
# Calculate the perimeter of a rectangle
length = 5
width = 3
perimeter = 2 * (length + width)
print("Perimeter of rectangle:", perimeter)     

