"""ATM Options Module"""
from banking_pkg.account import ATMOptions


print("          === Automated Teller Machine ===          ")

name = input("Enter name to register: ")
pin = input("Enter PIN: ")

BALANCE = 0
print(f"{name} has been registerd with a starting balance of ${float(BALANCE)}")
print("Login")

current_user = ATMOptions(BALANCE, name)

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if int(pin_to_validate) == int(pin) and name_to_validate == current_user.name:
        print("Success")
        break
    print("Invalid")


while True:
    current_user.atm_menu()
    current_user.show_balance()
    option = input("Choose an option: ")
    if option in ("1"):
        current_user.show_balance()
    if option in ("2"):
        amount = float(input("Amount to deposit: "))
        current_user.deposit(amount)
    if option in ("3"):
        amount = float(input("Amount to withdraw: "))
        current_user.withdraw(amount)
    if option in ("4"):
        current_user.logout()
        break
