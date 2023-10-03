class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Strongly private variable with double underscore

    def __str__(self):
        return f'Balance: {self.__balance}'

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Example usage:
account = BankAccount(1000)
print(account)
print("Current balance:", account.get_balance())
account.deposit(500)
print("Current balance:", account.get_balance())
account.withdraw(200)
print("Current balance:", account.get_balance())
print(account)
