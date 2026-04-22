# string is immutable 

# slicing 
# text  = "thisisjhalawar"
# print(text[::-2])
# print(text[0:5])



# split is used to split the string into a list based on the specified separator.
# text = "pizza  burger  pasta"
# print(text.split('  '))

# join is used to concatenate a list of strings into a single string, using a specified separator.
# text2 = ['z ', 'a', 'b', 'c', 'd']
# print(' '.join(text2))

s = "1234"
# isdigit() checks if all characters in the string are digits and there is at least one character. Since "1234" consists of digits, it returns True.
print(s.isdigit())   # True 

# isalpha() checks if all characters in the string are alphabetic (letters) and there is at least one character. Since "1234" consists of digits and no letters, it returns False.
print(s.isalpha())   # False

# isalnum() checks if all characters in the string are alphanumeric (either letters or digits) and there is at least one character. Since "1234" consists of digits, it returns True.
print(s.isalnum())   # True

# islower() checks if all characters in the string are lowercase letters and there is at least one character. Since "1234" consists of digits and no lowercase letters, it returns False.
print(s.islower())   # False


name = "Pintu"
age = 21

print("My name is {} and I am {} years old".format(name, age))