"""Import UI and user logic"""
import os
from donations_pkg import homepage_logic, user_logic

database = {"admin": "password123"}

donations = []
donors = None
authorized_user = None
TOTAL = 0.0


def init():
    homepage_logic.DonationMenu.show_homepage()


while True:
    init()
    if not authorized_user:
        print("You Must Be Logged in to donate")
    user_input = input("Choose an option: ")

    if user_input == "1":
        # Login
        user_login = input("Enter username: ")
        user_password = input("Enter Password: ")
        # instaniate new user from here
        authorized_user = user_logic.HandleUser(
            user_login, user_password, database)
        authorized_user.login()

    if user_input == "2":
        # Handle User Registration
        print("Registering new user...please proceed")
        name_to_register = input("Enter username: ")
        password_to_register = input("Enter password: ")
        authorized_user = user_logic.HandleUser(
            name_to_register, password_to_register, database)

        if authorized_user:
            authorized_user.register()

    if user_input == "3":
        # Donations
        if authorized_user:
            amount = float(input("Enter amount to donate: "))
            donors = homepage_logic.DonationMenu(
                username=authorized_user.username)
            if amount == 0:
                print("Amount must be greater than $0")

            else:
                TOTAL += donors.donate(amount)
                donations.append(donors.donation_to_str())

        else:
            print("Please login to donate")

    if user_input == "4":
        # Show Donations
        if authorized_user is None:
            print("Please login to see donations!")

        if authorized_user and len(donations) != 0:
            print("---ALL DONATIONS----")
            for donation in donations:
                print(donation)
            print(f"Total=${TOTAL}")

        if authorized_user and len(donations) == 0:
            print("Currently, there are no donations!")

    if user_input == "5":
        # Die
        os.system("clear")
        break
