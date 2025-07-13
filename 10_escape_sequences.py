# Escape Sequences in Python

# Escape sequences allow us to include special characters in strings
# These start with a backslash: \

# Example: String with tabs, quotes, and newlines
weather = "\tIt's \"kind of\" sunny\nHope you have a good day!"
print(weather)

# Other common escape sequences:
# \t - tab space
# \n - new line
# \' - single quote
# \" - double quote
# \\ - backslash

print("Line 1\nLine 2")  # \n creates a new line
print("Tabbed\tText")   # \t adds a tab space
print("Quotes: \"Hello\"")  # Use \\ or \" for special characters

# Using raw strings to ignore escape sequences
print(r"Raw string: C:\\Users\\Name")  # r before the string treats it as raw
print("Backslash: \\")  # Double backslash to show a single backslash
print("Unicode: \u03A9")  # Unicode character (Omega)
print("Hexadecimal: \x48\x65\x6C\x6C\x6F")  # Hexadecimal representation