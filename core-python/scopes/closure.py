def outer():
  x = 10
  print("Inside outer function, x =", x)
  def inner():
    print(x)
  return inner

closure = outer()
print(closure)  # This will print the inner function object

closure()  # This will print the value of x, which is 10 