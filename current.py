# Import Account class
from account import Account


class CurrentAccount(Account):

    def __init__(self, accountNumber,Name):
        super().__init__(accountNumber,Name)
        self.__fee = 1.75

        # override abstract function

    # deposit
    def deposit(self, amount):
        # Must be positive value
        if amount > 0:
            self._balance += amount
            self._balance -= self.__fee
            return True

        else:
            print("Error:Deposit amount must be positive")
            return False

    # withdraw function
    def withdraw(self, amount):

        # check positive value
        if amount > 0:
            # check sufficient balance
            if (self._balance + self.__fee) >= amount:
                self._balance -= amount
                self._balance -= self.__fee
            else:
                print("Error:Insufficient balance to withdraw")
        else:
            print("Error:Withdrawal amount must be positive")

    # Transfer function
    def transfer(self, to_account, amount):
        # check amount positive
        if amount > 0:

            if (self._balance + self.__fee) >= amount:
                to_account.deposit(amount)
                self._balance -= amount
                self._balance -= self.__fee

        else:
            print("Error:Transfer amount must be positive")
