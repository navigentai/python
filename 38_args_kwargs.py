# *args collects extra positional arguments
# **kwargs collects extra keyword arguments

def show_info(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

show_info("apple", "banana", size="large", color="yellow")
# Function with both *args and **kwargs
def display_data(*args, **kwargs):
    print("Items:", args)
    print("Details:", kwargs)

display_data(1, 2, 3, name="Alice", age=30)