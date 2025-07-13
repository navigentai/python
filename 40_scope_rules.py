# Python uses LEGB rule to resolve variable names:
# Local, Enclosing, Global, Built-in

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)

