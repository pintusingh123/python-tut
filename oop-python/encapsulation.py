# encapsulation is the concept of hiding the internal details of an object and only exposing s public interface.

# basic 
class Car:
  def __init__(self,brand,model):
    self.__brand = brand  #private attributes

    self.__model = model
  
  def get_brand(self):
    return self.__brand
  def get_model(self):
    return self.__model
  

obj1 = Car("tata", "nexon")
print(obj1.__model)  # This will raise an AttributeError
print(obj1.get_brand()) #OUTPUT tata
print(obj1.get_model()) #OUTPUT nexon


