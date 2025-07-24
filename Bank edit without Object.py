import random

#Functions
def dep(balance, depo_num):
    balance += depo_num
    return balance

def withdrow(balance, with_num):
    if with_num > balance:
        print("Invalid withdraw operation (Insufficient balance)")
        return balance
    return balance - with_num


def main_menu():
    banks = ["QNB", "Masr", "CIB"]
    accounts = {
        "Fouad": 1000
    }

    rand = random.choice(banks)
    print(f"Welcome to {rand} Bank!\n")

    while True:
        try:
            index = int(input("1: Login\n2: Sign Up\n3: Exit\nSelect: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if index == 1:
            name = input("Enter your account name: ")
            if name not in accounts:
                print("This name is not registered.")
                continue
            balance = accounts[name]
            print(f"Welcome {name}, your balance is {balance} EGP")

            
            while True:
                try:
                    operation = int(input("\n1: Check Balance\n2: Deposit\n3: Withdraw\n4: Logout\nSelect: "))
                except ValueError:
                    print("Enter a valid number.")
                    continue

                if operation == 1:
                    print(f"Your balance is {balance} EGP")
                elif operation == 2:
                    try:
                        amount = int(input("Enter amount to deposit: "))
                        balance = dep(balance, amount)
                        print(f"New balance: {balance} EGP")
                    except ValueError:
                        print("Enter a valid number.")
                elif operation == 3:
                    try:
                        amount = int(input("Enter amount to withdraw: "))
                        balance = withdrow(balance, amount)
                        print(f"New balance: {balance} EGP")
                    except ValueError:
                        print("Enter a valid number.")
                elif operation == 4:
                    accounts[name] = balance  
                    print("Logged out.\n")
                    break
                else:
                    print("Invalid option.")

        elif index == 2:
            name = input("Enter your name to create account: ")
            if not name:
                print("Name cannot be empty.")
                continue
            if name in accounts:
                print("Account already exists.")
                continue
            try:
                initial_balance = int(input("Enter initial balance: "))
                accounts[name] = initial_balance
                print(f"Account created for {name} with balance {initial_balance} EGP")
            except ValueError:
                print("Invalid balance amount.")

        elif index == 3:
            print("Thank you for using our bank. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


main_menu()
