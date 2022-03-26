from banking_pkg.account import BankOptions


def atm_menu(user):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + user)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

name = input("Enter name to register: ")
pin = input("Enter PIN: ")
BALANCE = 0
print(f"{name} has been registerd with a starting balance of ${float(BALANCE)}")
print("Login")

current_user = BankOptions(BALANCE, name)

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
    print(f"Current Balance: {current_user.show_balance()}")
    option = input("Choose an option: ")
    if option in ("1"):
        print(f"Current Balance: {current_user.show_balance()}")
    if option in ("2"):
        amount = float(input("Amount to deposit: "))
        current_user.deposit(amount)
    if option in ("3"):
        amount = float(input("Amount to widthdraw: "))
        current_user.widthdraw(amount)
    if option in ("4"):
        current_user.logout()
        break
