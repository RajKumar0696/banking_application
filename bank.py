class Bank(object):
    nextAccountNumber = 1000

    def __init__(self):
        self.__accounts = []

    def add_account(self, account):
        self.__accounts.append(account)

    def find_account(self, accountNumber):
        for account in self.__accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        return None

    def deposit(self, accountNumber, amount):
        account = self.find_account(accountNumber)
        if account is not None:
            if account.deposit(amount):
                print("Success: Transaction completed", accountNumber)
        else:
            print("Error: No such amount exist with account", accountNumber)

    def withdraw(self, accountNumber, amount):
        account = self.find_account(accountNumber)
        if account is not None:
            if account.withdraw(amount):
                print("Success: Transaction completed", accountNumber)
        else:
            print("Error: No such amount exist with account", accountNumber)

    def transfer(self, fromAccount, toAccount, amount):
        fromAccount = self.find_account(fromAccount)
        toAccount = self.find_account(toAccount)

        if fromAccount is not None and toAccount is not None:
            fromAccount.transfer(toAccount, amount)
            print("Successfully amount transfer ")
        else:
            print("Error:One of the To or From account doesn't exist")

    def checkBalance(self, accountNumber):
        account = self.find_account(accountNumber)
        if account is not None:
            print("Balance is:", account.getBalance())
        else:
            print("Error: No such account exist with account number:", accountNumber)

    @classmethod
    def getNextAccountNumber(cls):
        cls.nextAccountNumber += 1
        return cls.nextAccountNumber
