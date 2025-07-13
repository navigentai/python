# For loops repeat actions for each item in a sequence

colors = ["red", "green", "blue"]

for color in colors:
    print("Color:", color)

# Looping through numbers
for i in range(3):
    print("Number:", i)

# Looping through a string
word = "Python"
for letter in word:
    print("Letter:", letter)

# Using enumerate to get index and value
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")