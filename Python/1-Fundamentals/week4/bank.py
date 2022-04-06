class User:

    def __init__(self, name: str, pin: int, password: str) -> None:
        self.name = name
        self.pin = pin
        self.password = password

    def user_object(self) -> dict:
      user_credentials: dict = {"name": self.name,
                        "pin": self.pin, "password": self.password}
      return user_credentials
       
    def change_name(self, new_name: str) -> None:
        previous_name: str = self.user_object()["name"]
        if previous_name == new_name:
            print("You can't use the same name!")
            return None
        if len(new_name)<=2 or len(new_name)>=10:
           print("Name must be between 2 and 10 characters long!")
           return None
        self.name = new_name
        print("Name changed successful...")

    def change_pin(self, new_pin: int) -> None:
        previous_pin = self.user_object()["pin"]
        if str(previous_pin) == str(new_pin):
            print("You can't use the same pin!")
            return None
        if len(str(new_pin)) != 4:
            print("Pin must be 4 digits long!")
            return None
        self.pin = int(new_pin)
        print("Pin changed successful...")

    def change_password(self, new_password: str) -> None:
        previous_password: str = self.user_object()["password"]
        if previous_password == new_password:
            print("You can't use the same password!")
            return None
        if len(new_password) >=5: 
          self.password = new_password
        else:
            print("Password must be at least 5 characters long!")
            return None
        
        self.password = new_password
        print("Password changed successful...")


class BankUser(User):

    def __init__(self, name: str, pin: int, password: str) -> None:
        super().__init__(name, pin, password)
        self.balance: float = 0.00

        self.new_user_object = dict(self.user_object())
        self.new_user_object.update({"balance": self.balance})
    

    def validate_pin(self) -> bool:
        try:
            pin_to_authenticate: int = int(
                input("Please enter your pin: "))
            if pin_to_authenticate != self.pin:
                print("Incorrect PIN. Transaction cancelled")
                return False
            else:
                return True

        except ValueError:
            print("Try again!")

    def validate_password(self) -> bool:
        try:
            password_to_authenticate: str = input(
                "Please enter your password: ")
            if password_to_authenticate != self.new_user_object["password"]:
                print("Incorrect Password. Transaction cancelled")
                return False
            
            return True

        except ValueError:
            print("Try again!")

    def validate_amount(self, amount: float) -> bool:
        try:
            if amount < 0:
                print("Invalid amount")
                return False
        
            return True

        except ValueError:
            print("Please enter a valid amount!")

    def show_balance_after_transaction(self, user: User, bal: float) -> None:
        print(f"{user} has an account balance of: {bal}")

    def show_balance(self) -> None:
        print(f"{self.new_user_object['name']} has an account balance of: {self.new_user_object['balance']}")

    def deposit(self, amount: float) -> None:
        self.new_user_object['balance'] += amount
        self.show_balance()

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount):

          self.new_user_object['balance'] -= amount
          self.show_balance_after_transaction(self.new_user_object['name'], self.new_user_object['balance'])

    def transfer_money(self, other_user: User, amount: float) -> None:
        print(f"{self.new_user_object['name']} is transferring money to {other_user.name}: {amount}")

        if self.validate_pin() and self.validate_amount(amount):
            if amount > self.new_user_object['balance']:
                print("Insufficient funds to transfer")
                return None

        self.new_user_object['balance'] -= amount
        other_user.balance += amount
        print(f"{self.name} has an account balance of: {self.new_user_object['balance']}")
        self.show_balance_after_transaction(
            other_user.name, other_user.balance)

    def request_money(self, other_user: User, amount: float) -> None:
        print(f"You are requesting money from {other_user.name}: {amount}")
        print("User authentication required...")
    
        if self.validate_pin() and self.validate_password() and self.validate_amount(amount):
            if amount > other_user.balance:
              print(f"{other_user.name} has insufficient funds to widthdraw")
              return None

            self.new_user_object['balance'] += amount
            other_user.balance -= amount
            self.show_balance_after_transaction(self.new_user_object['name'], self.new_user_object['balance'])
            self.show_balance_after_transaction(
                other_user.name, other_user.balance)
            return None


bob = BankUser("Bob", 1234, "password")
bob.show_balance()
bob.deposit(1222)
bob.show_balance()

alice = BankUser("Alice", 4321, "password123")
alice.show_balance()
alice.deposit(100000.00)
alice.show_balance()
alice.request_money(bob, 123)
alice.transfer_money(bob, 1234.00)
bob.request_money(alice, 12.00)
bob.transfer_money(alice, 123.00)
bob.change_name("Bdddb")
bob.change_pin(3334)
