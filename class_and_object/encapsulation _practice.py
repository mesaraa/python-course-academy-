# Create a class BankAccount
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Method to get balance
    def get_balance(self):
        return self.__balance


# Create object of BankAccount
account = BankAccount(5000)

# Deposit and withdraw
account.deposit(1000)
account.withdraw(2000)

# Display balance
print("Current Balance:", account.get_balance())
