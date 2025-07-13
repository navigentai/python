# Formatted Strings in Python

# This allows you to insert variables inside strings easily and readably

# Using .format() method
name = 'Johnny'
age = 55

# Old way (with .format) - you provide values using names or positions
formatted_output = 'Hi {new_name}. You are {age} years old.'.format(new_name='Sally', age=100)
print(formatted_output)

# Using f-strings (modern and preferred way)
# f-strings let you directly embed variables inside curly braces
first_name = 'Anna'
user_age = 30
print(f'Hello {first_name}, you are {user_age} years old!')