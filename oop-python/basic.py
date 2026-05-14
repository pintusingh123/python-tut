# basic class and object in python 
class Person:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

p1 = Person("Toyota", "Camry")
print(p1.brand)
print(p1.model)

print(end="\n")

p2 = Person("honda", "civic")
print(p2.brand)
print(p2.model)