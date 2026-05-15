# create an electiccar class that inherits from the car class has an additional attribute called battery_size  

 

class Car:
  def __init__(self, name,model):
    self.name = name
    self.model = model
  def fullName(self):
   return f"my car is {self.name} {self.model}"

class ElectricCar(Car):
    def __init__(self, name, model, battery_size):

      super().__init__(name, model)
      self.battery_size = battery_size

my_tesla = ElectricCar("tesla", "model s", 100)
print(my_tesla.name)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.fullName())


# multiple inheritence
class A:
    def method_a(self):
        print("Method A from class A")

class B:
    def method_b(self):
        print("Method B from class B")

class C(A, B):
    
    def method_c(self):
        print("Method C from class C")


my_obj = C()
print(isinstance(my_obj, A)) #use isinstance() to check if my_obj is an instance of class A, B, or C
print(isinstance(my_obj, B))
print(isinstance(my_obj, C))