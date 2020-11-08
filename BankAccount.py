import random

class BankAccount:
      
      def __init__(self,full_name,account_number,routing_number,balance):
            self.full_name = full_name
            self._account_number = ": " + str(account_number)
            self.__routing_number = ": " + str(routing_number)
            self.balance = balance

      def deposit(self,amount):
            """ Display the amount of balance after a deposit """
            self.amount = amount
            self.balance += self.amount
            return print(f"Amount Deposited: ${self.amount}.\n")

      def withdraw(self,amount):
            """ Display the amount of balance after a withdrawal """
            self.amount = amount
            self.balance -= self.amount

            if self.balance <= 0:
              print(f"Balance: {self.balance}")
              self.balance -= 10
              return "Insufficient funds. Balance Charged $10.\n"
            else:
              print(f"Amount Withdrawn: ${self.amount}.")
              return "\n"

      def get_balance(self):
            return self.balance

      def add_interest(self):
            interest = self.balance * 0.00083
            return interest

      def print_receipt(self):
            receipt = {
              'Account no.':self._account_number,
              'Routing no.':self.__routing_number,
              'Balance':self.balance
            }
          
            bills = receipt.items()

            print(self.full_name)

            for bill,info in bills:
              print(bill,info)

            return ""

num1 = random.randint(000000000, 999999999)
num2 = random.randint(000000000, 999999999)
num3 = random.randint(000000000, 999999999)

reef = BankAccount("sharif stafford",num1,123456789,2)
leaf = BankAccount("leif erikson",num2,123456789,20)
bowe = BankAccount("david bowie",num3,123456789,2000)

print(reef.deposit(20))
print(reef.print_receipt())
print(leaf.withdraw(5))
print(leaf.print_receipt())
print(bowe.add_interest())
print(bowe.print_receipt())
