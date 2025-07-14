from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return f"The area of the rectangle is {self.length * self.width}"

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return f"The area of the circle is {math.pi * (self.radius ** 2)}"


r = Rectangle(20,20)
c= Circle(40)
print(c.area())
print(r.area())


class Account(ABC):
    def __init__(self, Account_holder, balance,account_type):
        self.account_holder = Account_holder
        self.balance = balance
        self.account_type = account_type

    @abstractmethod
    def calculate_interest(self):
        pass

class Saving_account(Account):
    def __init__(self, Account_holder, balance,account_type):
        super().__init__(Account_holder, balance,account_type)


    def calculate_interest(self):
        return self.balance * 0.05

    def display(self):
        interest = self.calculate_interest()
        return f"Account holder:{self.account_holder}\nAccount type:{self.account_type}\nBalance:{self.balance}\nInterest:{interest}"

class Current_account(Account):
    def __init__(self, Account_holder, balance,account_type):
        super().__init__(Account_holder, balance,account_type)


    def calculate_interest(self):
        return 0

    def display(self):
        interest = self.calculate_interest()
        return f"Account holder:{self.account_holder}\nAccount type:{self.account_type}\nBalance:{self.balance}\nInterest:{interest}"

Account_holder1 = Saving_account("Ali",10000,"Savings")
Account_holder2 = Current_account("Sara",20000,"Current")
print(Account_holder1.display())
print(Account_holder2.display())



class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    def warranty(self):
        return f"{1}year"

class Washing_machine(Appliance):
    def turn_on(self):
        return "now start."

    def display(self):
        return f"Washing machine is {self.turn_on()}\nWarranty={self.warranty()}"

class Air_conditioner(Appliance):
    def turn_on(self):
        return "now start."
    def display(self):
        return f"Air conditioner is {self.turn_on()}\nWarranty={self.warranty()}"

wm = Washing_machine()
Air_conditioner = Air_conditioner()
print(wm.display())
print(Air_conditioner.display())