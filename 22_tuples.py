# Tuples are like lists but immutable (unchangeable)

coordinates = (4, 5)

print("Coordinates:", coordinates)
print("X value:", coordinates[0])
print("Y value:", coordinates[1])

# Tuples can store mixed types
person_info = ("Taylor", 22, True)
print("Person info:", person_info)

# coordinates[0] = 10  # ❌ This will raise an error (tuples can't be changed)

# You can get the length of a tuple
print("Length of coordinates:", len(coordinates))

# Tuples support slicing
print("First element:", coordinates[0])
print("Last element:", coordinates[-1])     