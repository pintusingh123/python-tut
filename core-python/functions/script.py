def hello():
    return "Hi"

print(hello)      # <function hello at 0x...>
print(hello())    # Hi

print(len(hello()))  # 2

# 🔁 9. Recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))  # 120


# kwargs 
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(country="USA", language="Python")
print_kwargs()  # No arguments, should not print anything