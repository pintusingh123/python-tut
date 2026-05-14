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