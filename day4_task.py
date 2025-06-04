#OOPs
class atm:
    def __init__(self):

        self.pin=""
        self.balance=0
        self.withdraw=0
        self.menu()

    def menu(self):
        user_input=input("""
                    How would you like to proceed?
                    1- Enter 1 to Create pin
                    2- Enter 2 to deposit balance
                    3- Enter 3 to Withdraw
                    4- Enter 4 to Check balance
                    5- Enter 5 to Exit
                    
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdrawl()
        elif user_input == "4":
           self.balance_check()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter pin: ")

    def deposit(self):
        temp = input("Enter pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount: "))
            self.balance += amount
            print(f"{"Deposited successfully! "},Rs{self.balance}")
        else:
            print("ERROR, Your pn is incorrect")

    def withdrawl(self):
        temp = input("Enter pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount: "))
            if amount < self.balance:
                self.balance -= amount
                print("Withdraw successfully! ")
            else:
                print("Insufficient balance")
        else:
            print("ERROR, Your pin is incorrect")

    def balance_check(self):
        temp = input("Enter pin: ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("ERROR, Your pin is incorrect")

John=atm()
John.balance_check()
John.deposit()
John.balance_check()
John.withdrawl()



