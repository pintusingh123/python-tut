# lambda fun is a anonymous function which can take any number of arguments but can only have one expression. It is defined using the lambda keyword.

# syntax: lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
# lambda functions are often used in conjunction with higher-order functions like map(), filter(), and reduce().

# Example with map()
numbers = [1, 2, 3, 4, 5]
multi = lambda x: x ** 2
squared = list(map(multi, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example with filter()
numb = [1, 2, 3, 4, 5]
even = lambda x: x % 2 == 0
even_numbers = list(filter(even, numb))
print(even_numbers)  # Output: [2, 4]