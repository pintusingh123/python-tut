# static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables.


class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def general_des():
        return "This is a general description of the MathUtils class."

    
# Example usage
result1 = MathUtils.add(5, 3)
result2 = MathUtils.subtract(10, 4)
 
result3 = MathUtils.general_des()  
# This will work, but it's not a static method, so it should be called on an instance of the class.

print(result3)  # Output: This is a general description of the MathUtils class.
print("Addition:", result1)  # Output: Addition: 8
print("Subtraction:", result2)  # Output: Subtraction: 6