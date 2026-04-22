t = (5,)   # correct
m = (6,)    # correct

print(t,m)

p = (1, [2, 3])
p[1][0] = 100   # ✅ Allowed
p[1][1] = 200   # ✅ Allowed
print(p)
print("\n")

# example of tuple unpacking
t = 1,2,3  # this is a packing. tuple with three elements: 1, 2, and 3. The parentheses are optional when defining a tuple, so t is equivalent to (1, 2, 3).

a,  b, c = t # this is an example of tuple unpacking, where the values in the tuple t are assigned to the variables a, b, and c. After this line of code, a will be 1, b will be 2, and c will be 3.
print(a,b,c)

print("\n")
# advance unpacking 
a, b ,*c = (1,2,3,4,5,6)
print(a, b, c) # a will be 1 and b will be 2 and c will be [3, 4, 5, 6] because the * operator is used to unpack the remaining elements of the tuple into a list assigned to variable c.

print("\n")
# methods of touple
t = (1, 2, 2, 3)
print(t.count(9) ,t.index(3))  