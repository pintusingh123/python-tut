# find maximum between three numbers:
def find_max(a,b,c):
   if a >= b and a >= c:
      return f"a is maximum: {a}";
   elif b >= a and b>= c:
      return f"b is maximum: {b}";
   else:
      return f"c is maximum: {c}";

print(find_max(100,20,30))