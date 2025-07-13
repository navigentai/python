# Dictionaries store data in key-value pairs
# Keys must be unique and immutable (e.g., strings, numbers, tuples)

# Create a basic dictionary
user = {
    'name': 'Alice',
    'age': 30,
    'is_active': True
}

# Access values using keys
print("Name:", user['name'])
print("Age:", user['age'])

# Add a new key-value pair
user['email'] = 'alice@example.com'
print("After adding email:", user)

# Update an existing value
user['age'] = 31
print("After updating age:", user)

# Check if a key exists
if 'is_active' in user:
    print("User is active:", user['is_active'])

# Remove a key-value pair using pop
email = user.pop('email')
print("Removed email:", email)
print("After pop:", user)

# Get all keys
print("Keys:", list(user.keys()))

# Get all values
print("Values:", list(user.values()))

# Get all key-value pairs
print("Items:", list(user.items()))
