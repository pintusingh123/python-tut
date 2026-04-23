# sum of even numbers 
list_of_num = [1,2,3,4,5,6,7,8,9,10]

sum = 0; 
for num in list_of_num:
   if num % 2 == 0:
    sum = sum+num
    print(num, end=" ")

print("\nSum of even numbers:" ,sum)