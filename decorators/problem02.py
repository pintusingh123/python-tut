# create a decorator to print the funtion name and the value of thes argu every the the function is called
def debug(func):
  def wrapper(*args, **kwargs):
    args_value = ", ".join(str(arg) for arg in args)
    kwargs_value= ", ".join(f"{key}={value}" for key,value in kwargs.items())

    print(f"Function name: {func.__name__}")
    print(f"Arguments: {args_value}")
    print(f"Keyword Arguments: {kwargs_value}")

    return func(*args, **kwargs)
    
  return wrapper




@debug
def hello(name):
  print(f"hello, {name}")

@debug
def greet(name , greeting="hello bhai "):
  print(f"{greeting}, {name}")

hello("raja")
greet("pintuji ", greeting="hanji bhaiya")