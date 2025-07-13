# String Indexing and Slicing

selfish = '01234567'

# Each character has an index:
#  0 1 2 3 4 5 6 7
#  | | | | | | | |
#  0 1 2 3 4 5 6 7

# [start:stop] - stop is exclusive (not included)
print(selfish[0:8])  # prints all characters from index 0 to 7

# Shortcuts:
print(selfish[:4])   # from start up to index 3 → "0123"
print(selfish[4:])   # from index 4 to end → "4567"
print(selfish[:])    # whole string → "01234567"

# With steps: [start:stop:step]
print(selfish[0:8:2])  # every 2nd character → "0246"
print(selfish[::-1])   # reverse the string