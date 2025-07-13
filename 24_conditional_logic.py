# Use if, elif, and else to make decisions based on conditions

temperature = 30

if temperature > 35:
    print("It's very hot!")
elif temperature > 25:
    print("It's warm.")
elif temperature > 15:
    print("It's mild.")
else:
    print("It's cool.")

# You can also use boolean expressions
is_raining = False

if temperature > 25 and not is_raining:
    print("Great day for outdoor activities!")
elif is_raining:
    print("Don't forget your umbrella!")        