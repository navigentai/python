# In Python, some values are treated as False automatically

# Falsy values: "", 0, None, [], {}, set(), False
if "":
    print("This won't run (empty string is False)")
if 0:
    print("This won't run either (zero is False)")
if []:
    print("This won't run (empty list is False)")
if None:
    print("This won't run (None is False)")
if {}:
    print("This won't run (empty dict is False)")
if set():
    print("This won't run (empty set is False)")

# Truthy values: non-empty strings, non-zero numbers, non-empty collections
if "hello":
    print("This will run (non-empty string is True)")
if 42:
    print("This will also run (non-zero numbers are True)")
if [1, 2, 3]:
    print("This will run (non-empty list is True)")
if {1, 2}:
    print("This will run (non-empty set is True)")
if {"key": "value"}:
    print("This will run (non-empty dict is True)")