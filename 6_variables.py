# Variables store data that can change over time

name = "Taylor"   # str
age = 22          # int

print("Before update:", name, age)

# We can change their values later
name = "Morgan"
age = age + 1

print("After update:", name, age)

print("\n--- TYPES ---")
print("Type of name:", type(name))
print("Type of age:", type(age))

# Example: storing more info
is_student = True
hobbies = ["reading", "cycling", "coding"]

print("Is student:", is_student)
print("Hobbies:", hobbies)
print("Type of is_student:", type(is_student))
print("Type of hobbies:", type(hobbies))