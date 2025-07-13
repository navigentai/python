from functools import reduce

numbers = [1, 2, 3, 4, 5]
names = ['alice', 'bob', 'charlie']

# map: Square each number
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# filter: Get even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))    # Output: [2, 4]

# zip: Pair numbers with names
paired = zip(numbers, names)
print(list(paired))   # Output: [(1, 'alice'), (2, 'bob'), (3, 'charlie')]

# reduce: Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)          # Output: 15