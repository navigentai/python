# Strings have built-in methods that let you manipulate text

text = "  hello world  "

print(text.upper())       # HELLO WORLD
print(text.strip())       # Removes leading/trailing whitespace
print(text.replace("hello", "hi"))  # Replace part of the text
print("Length:", len(text))         # Count characters (including spaces)


print(text.split())       # Split into a list of words
print(text.split("o"))    # Split by 'o'
print(text.find("world")) # Find the index of "world"
print(text.startswith("  "))  # Check if it starts with spaces
print(text.endswith("  "))    # Check if it ends with spaces
print(text.isalpha())     # Check if all characters are alphabetic