# A matrix in Python is represented as a list of lists.
# Think of it as a grid or table with rows and columns.

# Create a 3x3 matrix (3 rows, 3 columns)
matrix = [
    [1, 2, 3],   # Row 0
    [4, 5, 6],   # Row 1
    [7, 8, 9]    # Row 2
]

# Print the full matrix
print("Full matrix:")
print(matrix)

# Access an element: matrix[row][column]
print("Element at row 1, column 2:", matrix[1][2])  # Output: 6

# Print a specific row
print("Second row:", matrix[1])

# Print all elements using nested loops
print("All elements in matrix:")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Line break after each row
