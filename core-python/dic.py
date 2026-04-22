# starting with chai our code with a dictionary
dic = {"name": "Alice", "age": 30, "city": "New York", "class": "python"}
print(dic)

# dic methods 
key = dic.keys() # keys() returns a view object that displays a list of all the keys in the dictionary. In this case, it will return dict_keys(['name', 'age', 'city', 'class']).
values = dic.values() # values() returns a view object that displays a list of all the values in the dictionary. In this case, it will return dict_values(['Alice', 30, 'New York', 'python']).
print(key)
print(values)

items = dic.items()
print(items)
 # items() returns a view object that displays a list of the dictionary's key-value pairs as tuples. In this case, it will return dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York'), ('class', 'python')]).

# updating the value of a key in the dictionary
dic.update({"age": 100}) # update() is a method that allows you to update the value of an existing key in the dictionary. In this case, it updates the value of the "age" key to 100. After this operation, the dictionary will be {'name': 'Alice', 'age': 100, 'city': 'New York', 'class': 'python'}.
print(dic)

# removing a key-value pair from the dictionary using the del statement
# del dic["age"]
# print(dic)
# dic.pop("name")
# dic.popitem()
# print(dic) 
# dic.popitem() 
# print(dic) 


# looping through a dictionary 

d = {
  "name": "Alice",
  "age": 30,
  "city": "New York",
  "class": "python"
}
print("looping\n")
# using for in loop 
for key in d :
   print(key, d[key]) # this will print the keys and values of the dictionary

print("values looping \n")
# using for in loop to print values
# using values() method to print values
#
for value in d.values()  :
    print(value) # this will print the values of the dictionary

print("values looping \n")

for key, value in d.items() :
    print(key,value)



print("formating squares\n") 
squares = {x: x**2 for x in range(1,10)}
print(squares)


print("\nNested dictionary\n")
students = {
    "pintu": {"age": 20, "marks": 85},
    "rahul": {"age": 21, "marks": 90}
}

print(students["pintu"]["marks"])