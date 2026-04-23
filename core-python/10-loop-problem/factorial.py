num = 5
numcopy = num
fact = 1;
while True:
   fact = fact * num
   num = num - 1; 
   if num == 0:
        break;
print("Factorial of", numcopy, "is:", fact)