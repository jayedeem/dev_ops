
def show_homepage():
    print("       === DonateMe Homepage ===       ")
    print("----------------------------------------")
    print("| 1. Login        | 2. Register        |")
    print("| 3. Donate       | 4. Show Donations  |")
    print("----------------------------------------")
    print("|             5. Exit                  |")
    print("----------------------------------------")


def donate(username: str):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = print(username, " donated ",
                            "${:,.2f}".format(donation_amt))
    print("Thank you for your donation")
    return donation_string
