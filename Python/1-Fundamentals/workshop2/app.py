'''This is ATM Module'''
from banking_pkg.account import ATMOptions

banking_user = ATMOptions()


def atm_menu(name: str) -> None:
    ''''
    atm menu
    '''
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
banking_user.name = input("Enter your name: ")
banking_user_pin = int(input("Enter Pin: "))

print(f"{banking_user.name} has been registered with a starting balance of ${banking_user.show_balance()}")
print("Login")

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = int(input("Enter Pin: "))
    if name_to_validate != banking_user.name and pin_to_validate != banking_user_pin:
        print("Invalid")
    else:
        print("Success")
        break

while True:
    atm_menu(banking_user.name)
    banking_user.show_balance()
    option = input("Choose an option: ")

    if option in ("1"):
        print(f"Current balance ${banking_user.show_balance()}")

    if option in ("2"):
        amount = float(input("Amount to deposit: "))
        banking_user.deposit(amount)

    if option in ("3"):
        amount = float(input("Amount to withdraw: "))
        banking_user.withdraw(amount)

    if option in ("4"):
        banking_user.logout()
        break
