# from banking_pkg.account import BankOptions


class BankOptions:

    def __init__(self, current_balance=0.0, user_name=""):
        self.current_balance = current_balance
        self.user_name = user_name

    def show_balance(self):
        return self.current_balance

    def deposit(self, amount):
        self.current_balance += amount

    def widthdraw(self, amount):
        self.current_balance -= float(amount)

    def logout(self):
        print(f"Goodbye! {self.user_name}")


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registerd with a starting balance of ${int(balance)}")
print("Login")

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate != name and pin_to_validate != pin:
        print("Invalid")
    else:
        print("Success")
        break

while True:
    atm_menu(name)
    option = int(input("Choice an option: "))
    user_opt = BankOptions()

    if option == 1:
        print(f"Current Balance: ${user_opt.show_balance()}")
    if option == 2:
        deposited_amount = float(input("Enter amount to deposit: "))
        user_opt.deposit(deposited_amount)
        print(user_opt.balance)
    if option == 3:
        widthdraw = int(input("Enter Amount to Widthdraw: "))
        user_opt.widthdraw(widthdraw)
        print(f"Current Balance: {user_opt.show_balance()}")
