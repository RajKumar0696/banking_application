# Import ABC abstract method

from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, accountNumber,Name):
        self.__accountNumber = accountNumber
        self._balance = 0.0
        self.Name=Name

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, to_account, amount):
        pass

    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self._balance
