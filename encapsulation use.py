#ENCAPSULATION

class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        return f"Deposited {amount}.The total balance is: {self.__balance}"

    def withdraw(self,amount):
        if self.__balance-amount<0:
            return "Transaction failed!You don't have enough money."
        else:
            self.__balance-=amount
            return f"Withdrawn {amount}. The total balance is: {self.__balance}"

    def get_balance(self):
        return f"{self.name} current balance is {self.__balance}Rs"

    def display(self):
        return f"{self.name}'s balance is {self.__balance}"

user=Bankaccount("Lionel",10000)
print(user.get_balance())
print(user.deposit(100))
print(user.withdraw(1000))
print(user.display())
