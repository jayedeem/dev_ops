"""Mock banking system"""


class User:
    """Define a User Object"""

    def __init__(self, name: str, pin: int, password: str) -> None:
        self.name: str = name
        self.pin: int = pin
        self.password: str = password
        self.data: dict = {"name": self.name,
                           "pin": self.pin, "password": self.password}

    def change_name(self, new_name: str) -> None:
        """Change User name"""
        previous_name: str = self.data["name"]
        if previous_name == new_name:
            print("You can't use the same name!")
            return
        if len(new_name) <= 2 or len(new_name) >= 10:
            print("Name must be between 2 and 10 characters long!")
            return
        self.data['name'] = new_name.strip()
        print("Name changed successful...")

    def change_pin(self, new_pin: int) -> None:
        """Change Pin"""
        previous_pin = self.data["pin"]
        if str(previous_pin) == str(new_pin):
            print("You can't use the same pin!")
            return
        if len(str(new_pin)) != 4:
            print("Pin must be 4 digits long!")
            return
        self.data['pin'] = int(new_pin)
        print("Pin changed successful...")

    def change_password(self, new_password: str) -> None:
        """Change Password"""
        previous_password: str = self.data["password"]
        if previous_password == new_password:
            print("You can't use the same password!")
            return
        if len(new_password) >= 5:
            self.data['password'] = new_password
            print("Password changed successful...")
        else:
            print("Password must be at least 5 characters long!")
            return


class BankUser(User):
    """Define Bank User child"""

    def __init__(self, name: str, pin: int, password: str) -> None:
        super().__init__(name, pin, password)
        self.balance: float = 0.00
        self.data['balance'] = self.balance

    def validate_pin(self) -> bool:
        """Pin validation"""
        try:
            pin_to_authenticate: int = int(
                input("Please enter your pin: "))
            if pin_to_authenticate != self.pin:
                print("Incorrect PIN. Transaction cancelled")
                return False
            return True
        except ValueError:
            print("Try again!")
            return False

    def validate_password(self) -> bool:
        """Password validaton"""
        try:
            password_to_authenticate: str = input(
                "Please enter your password: ")
            if password_to_authenticate != self.data["password"]:
                print("Incorrect Password. Transaction cancelled\n")
                return False
            return True

        except ValueError:
            print("Try again!")
            return False

    def validate_amount(self, amount: float) -> bool:
        """Validate amount < 0"""
        try:
            if amount < 0:
                print("Invalid amount")
                return False
            return True

        except ValueError:
            print("Please enter a valid amount!")
            return False

    def show_balance_after_transaction(self, user: User) -> str:
        """Display balance after transaction"""
        print(
            f"{user.data['name']} has a balance of ${user.data['balance']}\n")

    def show_balance(self) -> str:
        """Show balance"""
        return print(
            f"{self.data['name']} has an account balance of: {self.data['balance']}\n")

    def deposit(self, amount: float) -> None:
        """Deposit"""
        self.data['balance'] += amount
        self.show_balance_after_transaction(self)

    def withdraw(self, amount: float) -> bool:
        """Withdraw"""
        if self.data['balance'] < amount:
            print('Insufficent Funds')
            return False

        self.data['balance'] -= amount
        self.show_balance_after_transaction(self)
        return True

    def transfer_money(self, other_user: User, amount: float) -> None:
        """Transfer Money"""
        print(
            f"{self.data['name']} initiated a transfer to {other_user.name} of ${amount}\n")

        if self.validate_pin():
            if self.validate_amount(amount) and self.withdraw(amount):
                other_user.deposit(amount)
                self.show_balance_after_transaction(user=other_user)
                self.show_balance_after_transaction(user=self)
                print("Transaction Successful...")

    def request_money(self, other_user: User, amount: float) -> None:
        """Request Money"""
        print(
            f"{self.data['name']} is requesting funds from {other_user.name} of ${amount}\n")
        print("User authentication required....")
        if self.validate_amount(amount) and self.validate_pin() and self.validate_password():
            if other_user.withdraw(amount):
                self.deposit(amount)
                print("Transaction Successful...")


bob = BankUser(name="Bob", pin=1234, password="password")
bob.change_pin(2311)
bob.change_password("pass123sdfasf4")
# bob.deposit(amount=10.00)
# alice = BankUser(name="Alice", pin=4321, password="password123")
# alice.deposit(amount=200.00)
# bob.request_money(other_user=alice, amount=1.00)
# bob.transfer_money(other_user=alice, amount=1.00)
# alice.show_balance()
# bob.show_balance()
