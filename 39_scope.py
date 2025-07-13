# Variables have scope — where they are visible in code

name = "Task Update"

def say_name():
    name = "Task Update"
    print("Inside function:", name)

say_name()
print("Outside function:", name)

# Methods are functions that belong to an object