username = "chaitanya"

def greet():
   name = "alice"

   def get_greeting(): 
      username = "bob"
      print(username)
      return "hello " + name
   
   return get_greeting()

print(greet())


# second example
# print(end="\n")
# x = 10
# def greet2(y):
#     z = x+y
#     return z
# result = greet2(5);
# print(result)

# third example
print(end="\n")
def greet3():
    x = 889
    
    def inner():
       print(x) 

    inner()
 
greet3()
