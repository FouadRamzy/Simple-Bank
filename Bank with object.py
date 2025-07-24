class Bank:
    def __init__(self, Account, Balance=0):
        self.Account = Account
        self.Balance = Balance

    def deposite(self, Amount):
        self.Balance += Amount
        print(f"You deposited {Amount}. Your balance is now {self.Balance}")

    def withdrow(self, Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
            print(f" You withdrew {Amount}. Your balance is now {self.Balance}")
        else:
            print(" Error: Withdrawal amount is greater than your balance.")

    def operation(self):
        while True:
            try:
                index = int(input("\nChoose operation:\n1 - Check Balance\n2 - Withdraw\n3 - Deposit\n4 - Exit\nYour choice: "))
                if index == 1:
                    print(f" Your balance is: {self.Balance}")
                elif index == 2:
                    wit = int(input("Enter amount to withdraw: "))
                    self.withdrow(wit)
                elif index == 3:
                    depo = int(input("Enter amount to deposit: "))
                    self.deposite(depo)
                elif index == 4:
                    print("Exiting......")
                    break
                else:
                    print(" Invalid option.")
            except ValueError:
                print(" Please enter a valid number.")


import random

banks = ["QNB", "CIB", "HSBC"]
bank_name = random.choice(banks)
print(f" Welcome to {bank_name} Bank")

accounts_list = [Bank("Fouad", 1000)]  # Default account

op = int(input("\nMain Menu:\n1 - Login\n2 - Sign Up\nYour choice: "))

if op == 1:
    user = input("Enter your username: ")
    found = False
    for acc in accounts_list:
        if acc.Account == user:
            print(f" Welcome back, {user}")
            acc.operation()
            found = True
            break
    if not found:
        print(" Sorry, user not registered.")

elif op == 2:
    user = input("Enter a username to create account: ")
    balance = int(input("Enter initial balance: "))
    new_acc = Bank(user, balance)
    accounts_list.append(new_acc)
    print(f" Account created for {user}")
    new_acc.operation()

else:
    print(" Invalid choice.")
