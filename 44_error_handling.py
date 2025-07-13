def authenticated(func):
    def wrapper(*args, **kwargs):
        user = {'is_logged_in': True}  # Simulate user state
        if user.get('is_logged_in'):
            return func(*args, **kwargs)
        else:
            return "Please log in first"
    return wrapper

@authenticated
def sensitive_data():
    return "Sensitive info: Access granted"

print(sensitive_data())  # Output: Sensitive info: Access granted