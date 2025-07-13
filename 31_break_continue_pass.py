# break: exits the loop early
# continue: skips the current iteration
# pass: does nothing (used as a placeholder)

# Example: continue (skip a value)
for number in range(5):
    if number == 3:
        continue  # Skip 3
    print("Number:", number)

print("----")

# Example: break (exit loop early)
for number in range(5):
    if number == 4:
        break  # Stop loop at 4
    print("Number:", number)

print("----")

# Example: pass (placeholder for future code)
def unfinished_function():
    pass  # You can define the function without writing code yet

# Using pass in a loop
for i in range(3):
    if i == 1:
        pass  # Placeholder, does nothing
    else:
        print("Loop iteration:", i)