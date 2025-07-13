# Indentation (spacing) is required to structure code in Python

x = 10

if x > 5:
    print("x is greater than 5")      # This block belongs to the 'if'
    print("Still inside if block")
    if x > 8:
        print("x is also greater than 8")  # Nested block

print("Outside of the if block")  # This line is outside