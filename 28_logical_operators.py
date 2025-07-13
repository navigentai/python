# Logical operators: and, or, not

has_account = True
is_verified = False

if has_account and is_verified:
    print("Access granted")
else:
    print("Access denied")

if not is_verified:
    print("Please verify your account.")

# More examples
age = 20
is_active = True

if age >= 18 and is_active:
    print("Adult and active user")

if has_account or is_verified:
    print("At least one requirement met for limited access")