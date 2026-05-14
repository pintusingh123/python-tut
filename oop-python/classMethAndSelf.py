# class method and self ( add a method to the person class that display the ful name of the car)
class Person:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fullName(self):
    return f"{self.brand} {self.model}"

p1 = Person("tata", "nexon")
print(p1.fullName())