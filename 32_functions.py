# A function is a reusable block of code that performs a task

def say_hello():
    print("Hello there!")

# Call the function multiple times
say_hello()
say_hello()

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Taylor")
greet("Morgan")

# Function that returns a value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)