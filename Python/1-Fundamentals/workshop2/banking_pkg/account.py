'''This is ATM Module'''


class ATMOptions:
    '''
    ATM Options
    '''
    # init construct

    def __init__(self, balance=0.0, name="") -> None:
        self.balance = balance
        self.name = name

    def show_balance(self) -> float:
        '''
        show_balance
        return balance
        '''
        print("${:,.2f}".format(self.balance))
        return self.balance
# depost

    def deposit(self, amount) -> None:
        '''
        deposit
        '''
        self.balance += amount

# widthdraw
    def withdraw(self, amount) -> None:
        '''
        withdraw
        '''
        self.balance -= amount

# logout
    def logout(self) -> None:
        '''
        logout
        '''
        print(f"Goodbye {self.name}")
