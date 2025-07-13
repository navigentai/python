# List slicing allows you to get a portion of a list using the [start:stop] syntax

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Get the first three elements (index 0 up to but not including 3)
print("First three:", my_list[0:3])

# Get from the beginning to index 4 (not including 4)
print("Start to index 4:", my_list[:4])

# Get from index 2 to the end
print("From index 2 to end:", my_list[2:])

# Get the whole list using slicing
print("Full list:", my_list[:])

# Get every second element
print("Every second element:", my_list[::2])

# Reverse the list using slicing
print("Reversed list:", my_list[::-1])
