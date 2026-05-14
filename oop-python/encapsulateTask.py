class BackBalancer:
   def __init__(self,balance):
      self.__balance = balance
  
   def show_balance(self):
    return f"your balance is {self.__balance}"
  # balance update/set 
   def update_balance(self, amount):
    #  self.__balance += amount
     if amount > 0:
            self.__balance = amount
            print(f"Balance updated to {self.__balance}")
     if amount < 0:
         print("Invalid amount")
    
  #  withraw balance
   def withdraw_balance(self, amount):
      if amount > self.__balance:
          print("Insufficient balance")
      else:
          self.__balance -= amount
          print(f"Balance after withdrawal: {self.__balance}")

obj1 = BackBalancer(1000)
print(obj1.show_balance())  #OUTPUT your balance is 1000
obj1.update_balance(2000)  #OUTPUT Balance updated to 2000
print(obj1.show_balance())  #OUTPUT your balance is 2000
obj1.withdraw_balance(500)  #OUTPUT Balance after withdrawal: 1500
print(obj1.show_balance())  #OUTPUT your balance is 1500