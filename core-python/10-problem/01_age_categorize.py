#01_ problem: Age Group Categorization
# classify a person's age group: child ( < 13), teenager (13-19), adult (20-64), senior (65+)

age  = int(input("Enter Your Age: "))
if age < 13 :
   print("your are a child")
if age >= 13 and age <= 19 :
   print("your are a teenager")
if age >=20 and age <60 :
   print("you are an adult")
if age >= 65 :
   print("you are a senior")