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