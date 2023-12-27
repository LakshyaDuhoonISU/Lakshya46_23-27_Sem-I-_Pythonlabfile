#WAP to create the Bank Module to perform the operations such as Check the Balance, withdraw and deposit the money in bank account and import the module in main file.
from bank_module import ATM
b=ATM()
while True:
    a=int(input("Press 1 to deposit\nPress 2 to withdraw\nPress 3 to check balance\nPress 4 to Exit\n"))
    if a==1:
        b.deposit()
    elif a==2:
        b.withdraw()
    elif a==3:
        b.check()
    elif a==4:
        print("Thank You")
        break
    else:
        print("Invalid choice\n")