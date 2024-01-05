#WAP to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = {'holder': account_holder, 'balance': initial_balance}
            print(f"Account created for {account_holder} with account number {account_number}")
        else:
            print(f"Account with account number {account_number} already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited {amount} into account {account_number}. New balance: {self.accounts[account_number]['balance']}")
        else:
            print(f"Account with account number {account_number} not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]['balance']}")
            else:
                print(f"Insufficient funds in account {account_number}.")
        else:
            print(f"Account with account number {account_number} not found.")
    
    def display_account(self, account_number):
        if account_number in self.accounts:
            print(f"Account Number: {account_number}, Holder: {self.accounts[account_number]['holder']}, Balance: {self.accounts[account_number]['balance']}")
        else:
            print(f"Account with account number {account_number} not found")

    def display_accounts(self):
        print("Accounts:")
        for acc_num, acc_info in self.accounts.items():
            print(f"Account Number: {acc_num}, Holder: {acc_info['holder']}, Balance: {acc_info['balance']}")

def main():
    bank = Bank()
    while True:
        print("1.Create Account")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Display all accounts")
        print("5.Display a particular account")
        print("6.Exit")
        a=int(input("Enter choice: ")) 
        if a==1:
            b=int(input("Enter account number: "))
            c=input("Enter name of account holder: ")
            d=int(input("Enter account balance: "))
            bank.create_account(b,c,d)
        elif a==2:
            b=int(input("Enter account number: "))
            d=int(input("Enter amount to deposit: "))
            bank.deposit(b,d)
        elif a==3:
            b=int(input("Enter account number: "))
            d=int(input("Enter amount to withdraw: "))
            bank.withdraw(b,d)
        elif a==4:
            bank.display_accounts()
        elif a==5:
            b=int(input("Enter account number: "))
            bank.display_account(b)
        elif a==6:
            print("Exiting. Thank You!")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()