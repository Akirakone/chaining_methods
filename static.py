
class User:	
    def __init__(self, name):
        self.name = name
        self.balance = 0
    # adding the deposit method
    def withdraw(self,amount):
            self.balance -=amount
            return self
    def deposit(self, amount):
        self.balance +=amount
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, balance: {self.balance}")

Akira = User("Akira")
ousmane=User("ousmane")
crystal=User("crystal")
        
Akira.deposit(500).deposit(750).deposit(900).deposit(10).withdraw(550)
Akira.display_user_balance ()

ousmane.deposit(1000).deposit(50).deposit(9000).withdraw(100).withdraw(5000)
ousmane.display_user_balance ()

crystal.deposit(500).deposit(50).withdraw(500).withdraw(110).withdraw(250)
crystal.display_user_balance ()