from donations_pkg.homepage import show_homepage
from donations_pkg.user import login

database = {"admin": "password123"}

donations = []

authorized_user = ""

if not authorized_user:
    show_homepage()
    print("You must be logged in to donate")
else:
    print(f"Logged in as {authorized_user}")

# available_options = {1: login,
#                      2: "TODO Write Register Functionality",
#                      3: "TODO Write Donate Functionality",
#                      4: "TODO Write Show Donation Functionality",
#                      5: "Goodbye"}

user_options = int(input("Choose an option: "))
if user_options == 1:
    authorized_user = input("Enter username: ")
    authorized_user_password = input("Enter password: ")
    login(database, authorized_user, authorized_user_password)
