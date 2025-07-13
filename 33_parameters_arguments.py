# Functions can accept input values called parameters

def greet(name):
    print(f"Hi, {name}!")

greet("Sam")
greet("Taylor")

# Function with multiple parameters
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Sam", 25)
introduce("Taylor", 30)

# Function with a default parameter value
def welcome(name="Guest"):
    print(f"Welcome, {name}!")