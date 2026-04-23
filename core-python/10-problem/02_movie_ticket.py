# Movie Ticket Pricing
# A movie theater charges different ticket prices based on a person's age. If a person is under the age of 3, the ticket is free. If they are between the ages of 3 and 12, the ticket is $10. If they are over the age of 12, the ticket is $15. Write a program that asks the user for their age and then prints out the cost of their movie ticket.
age = int(input("Enter Your Age: "))
if age < 3 :
   print("your ticket is free")
elif age <= 12 :
    print("your ticket is $10")
else :
    print("your ticket is $15")

