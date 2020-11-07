import random

class BankAccount:
    def __init__(self,full_name,account_number,routing_number,balance):
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self.balance = balance

        return

    def deposit(self,amount):
        """ Display the amount of balance after a deposit """
        self.amount = amount
        self.balance += self.amount
        print(f"Amount Deposited: ${self.amount}.")

        return f"Balance: {self.balance}"

    def withdraw(self,amount):
        """ Display the amount of balance after a withdrawal """
        self.amount = amount
        self.balance -= self.amount

        if self.balance <= 0:
          self.balance -= 10
          return print("Insufficient funds. Balance Charged $10")
        else:
          print(f"Amount Withdrawn: ${self.amount}.")
          return (f"Balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        return interest

    def print_receipt(self):
      name = self._full_name
      
      receipt = {
        'Account no.' : self._account_number,
        'Routing no.' : self._routing_number,
        'Balance' : self.balance
      }

      print(name)

      for receipts in receipt:
        print(receipts)

      return print ('\n')

    

num1= random.randint(000000000, 999999999)
num2= random.randint(000000000, 999999999)
num3= random.randint(000000000, 999999999)

reef = BankAccount("sharif stafford",num1,123456789,20)
leaf = BankAccount("leif erikson",num2,123456789,20)
bowe = BankAccount("david bowie",num3,123456789,20)

print(reef.print_receipt())
print(leaf.print_receipt())
print(bowe.print_receipt())
