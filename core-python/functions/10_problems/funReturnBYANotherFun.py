# 8. Function returning another function
 
def outer():
    def inner():
        return "Hello"
    return inner


greet = outer()  # greet is now the inner function
print(greet())  # Output: Hello