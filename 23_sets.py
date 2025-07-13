# Sets store unique, unordered values

items = {1, 2, 3, 3, 2}
print("Set contents:", items)  # Duplicates are removed

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)         # {1, 2, 3, 4, 5}
print("Intersection:", a & b)  # {3}
print("Difference (a - b):", a - b)  # {1, 2}
print("Symmetric difference:", a ^ b)  # {1, 2, 4, 5}

# Add and remove elements
a.add(6)
print("After adding 6 to a:", a)
a.discard(2)
print("After discarding 2 from a:", a)

# Check membership
print("Is 3 in a?", 3 in a)
print("Is 4 in a?", 4 in a)
print("Is 7 in a?", 7 in a)             