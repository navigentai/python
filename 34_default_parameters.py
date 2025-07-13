# You can give a parameter a default value

def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()         # Uses the default: Guest
greet("Jordan") # Uses the provided name

# Function with multiple default parameters
def introduce(name="Guest", age=0):
    print(f"{name} is {age} years old.")

introduce()                 # Guest is 0 years old.
introduce("Jordan")         # Jordan is 0 years old.
introduce("Jordan", 25)     # Jordan is 25 years old.