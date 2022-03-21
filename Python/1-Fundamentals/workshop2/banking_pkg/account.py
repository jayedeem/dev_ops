class BankOptions:

    def __init__(self, balance=0, name=""):
        self.balance = balance
        self.name = name

    def show_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def widthdraw(self, amount):
        self.balance -= float(amount)

    def logout(self):
        print(f"Goodbye! {self.name}")
