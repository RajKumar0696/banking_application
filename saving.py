from account import Account


class SavingsAccount(Account):
    def __init__(self, accountNumber,Name):
        super().__init__(accountNumber,Name)
        self.__ir = 0.0375

    # deposit
    def deposit(self, amount):
        # Must be positive value
        if amount > 0:
            self._balance += amount
            return True

        else:
            print("Error:Deposit amount must be positive")
            return False

    # withdraw function
    def withdraw(self, amount):

        # check positive value
        if amount > 0:
            # check sufficient balance
            if self._balance >= amount:
                self._balance -= amount
            else:
                print("Error:Insufficient balance to withdraw")
        else:
            print("Error:Withdrawal amount must be positive")

    # Add interest rate into the account
    def apply_interest(self):
        interest = self._balance * self.__ir
        self.deposit(interest)

    # Transfer function
    def transfer(self, to_account, amount):
        # check amount positive
        if amount > 0:

            if self._balance >= amount:
                to_account.deposit(amount)
                self._balance -= amount
            else:
                print("Error:Transfer amount must be positive")
