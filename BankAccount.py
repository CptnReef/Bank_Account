class BankAccount:
    def __init__(self,full_name,account_number,routing_number,balance):
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self.balance = balance

    def deposit(self,amount):
        """ Display the amount of balance after a deposit """
        self.amount = amount
        balance = self.amount + self.balance
        print(f"Amount Deposited: ${self.amount}.")
        return balance

    def withdraw(self,amount):
        """ Display the amount of balance after a withdrawal """
        self.amount = amount
        balance = self.balance - self.amount

        if balance <= 0:
          print(f"Insufficient funds.")
          balance -= 10
        else:
          print(f"Amount Withdrawn: ${self.amount}.")

        return balance



reef = BankAccount("sharif stafford",111111111,1,20)
print(reef.deposit(10))
print(reef.withdraw(20))
