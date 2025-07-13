# Docstrings describe what a function does

def greet():
    """Prints a simple greeting message."""
    print("Hello!")

greet()  # Calls the function and prints "Hello!"
print(greet.__doc__)  # Prints the docstring: "Prints a simple greeting message."
