class BankAccount:
    def __init__(self,full_name,account_number,routing_number,balance):
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self._balance = balance

    def deposit(self, amount):
        """ Display the amount of balance after a deposit """
        self.amount = amount
        print( f"You have deposited {self.amount}. into your Bank Account Your remaining balance is" )

    def withdraw(self):
        """ Display the amount of balance after a withdrawal """

reef = BankAccount("sharif stafford",1,1,0)

print(reef.deposit(10))
print(reef)
print("hi")