# Python lists come with built-in methods to manipulate the list

# Create a basic list
fruits = ['apple', 'banana', 'cherry']

# Add an item to the end of the list
fruits.append('orange')
print("After append:", fruits)

# Insert an item at a specific position
fruits.insert(1, 'grape')
print("After insert at index 1:", fruits)

# Remove an item by value
fruits.remove('banana')
print("After remove 'banana':", fruits)

# Remove and return the last item
last_item = fruits.pop()
print("After pop:", fruits)
print("Popped item:", last_item)

# Find the index of an item
index = fruits.index('apple')
print("Index of 'apple':", index)

# Count how many times an item appears
count = fruits.count('apple')
print("Count of 'apple':", count)

# Sort the list in alphabetical order
fruits.sort()
print("Sorted list:", fruits)

# Reverse the order of the list
fruits.reverse()
print("Reversed list:", fruits)

# Clear all elements from the list
fruits.clear()
print("Cleared list:", fruits)
