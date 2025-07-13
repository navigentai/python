# Math Functions in Python

# Python provides built-in math functions and the math module for advanced operations.

import math

x = 16
y = -4.5

print("--- BUILT-IN FUNCTIONS ---")
print("Rounding 3.9:", round(3.9))           # Rounds to nearest integer
print("Absolute value of y:", abs(y))         # Always positive
print("Max of 4, 9, 2:", max(4, 9, 2))       # Largest value
print("Min of 4, 9, 2:", min(4, 9, 2))       # Smallest value
print("Power: 3^3 =", pow(3, 3))             # 3 raised to 3

print("\n--- MATH MODULE FUNCTIONS ---")
print("Square root of x:", math.sqrt(x))      # Square root
print("Pi constant:", math.pi)                # Pi value
print("Ceiling of y:", math.ceil(y))          # Round up
print("Floor of y:", math.floor(y))           # Round down
print("Power: 2^5 =", math.pow(2, 5))         # 2 raised to 5

print("\n--- EXERCISES ---")
# Use math.pow() to find 2 raised to the power of 5
print("2^5 using math.pow:", math.pow(2, 5))

# Use round() to round 5.678 to 1 decimal place
print("Round 5.678 to 1 decimal:", round(5.678, 1))

# Use math.sqrt() to find the square root of a number
num = 49
print("Square root of", num, "is", math.sqrt(num))

