a = 10
b = 20

print(a - b)
# gives logical error because we want to get the sum but we are getting the difference of a and b. 
# no code crashes but the output is not what we expected.

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    print(10 / 0)

except Exception as e:
    print(e) 

# finally block is used to execute the code that must be executed whether an exception occurs or not.
try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Always executes")