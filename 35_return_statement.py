# Functions can return values using return

def add(x, y):
    return x + y

result = add(5, 7)
print("Sum:", result)

# Function that returns multiple values
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(10, 3)
print("Quotient:", q)
print("Remainder:", r)

# Function that returns a boolean
def is_even(n):
    return n % 2 == 0

print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))