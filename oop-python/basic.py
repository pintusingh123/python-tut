# basic class and object in python 
class Person:

  
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def show(self):
    print(self)
    # print(f"brand: {self.brand}, model: {self.model}")

p0 = Person("onex", "twox")
p0.show()   #output: <__main__.Person object at 0x7f8c8c8c8c8c>

print(end="\n")

p1 = Person("Toyota", "Camry")
print(p1.brand)
print(p1.model)

print(end="\n")

p2 = Person("honda", "civic")
print(p2.brand)
print(p2.model)