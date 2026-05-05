def Is_even(num):
   if num <= 0 :
      return "Neither even or odd";
   if num % 2 == 0:
      return "Even";
   else:
      return "odd"
   
print(Is_even(-10))