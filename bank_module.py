class ATM:
    __balance=50000
    __pin=0
    __name=""
    def __init__(self):
        print("Welcome to ABC Bank")
        self.__pin=int(input("Enter your PIN: "))
        self.__name=input("Enter your name: ")
    def deposit(self):
        a=float(input("Enter amount to deposit: "))
        if a<=0:
            print("Invalid amount\n")
        else:
            print("Successfully deposited Rs",a,"cash\n")
            self.__balance+=a
    def withdraw(self):
        a=float(input("Enter amount to withdraw: "))
        if a<=0 or a>self.__balance:
            print("Invalid amount\n")
        else:
            print("Successfully withdrew Rs",a,"cash\n")
            self.__balance-=a
    def check(self):
        print("Balance: Rs", self.__balance)
        print(f"Your Account Number XXXXXXXX{self.__pin}\n")