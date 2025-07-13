# -------------------------------
# String Immutability in Python
# -------------------------------

selfish = '01234567'

# Strings are immutable, meaning we cannot change them in place.
# Instead, we create a new string by combining existing strings.

selfish = selfish + '8'  # This creates a *new* string in