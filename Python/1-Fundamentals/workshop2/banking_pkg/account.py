'''This is ATM Module'''


class ATMOptions:
    '''
    ATM Options
    '''
    # init construct

    def __init__(self, balance=0.0, name="") -> None:
        self.balance = balance
        self.name = name

    def atm_menu(self):
        '''ATM MENU'''
        print("")
        print("          === Automated Teller Machine ===          ")
        print("User: " + self.name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")

    def show_balance(self) -> float:
        '''
        show_balance
        return balance
        '''
        print("Current Balance: ${:,.2f}".format(self.balance))
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
        if amount > self.balance:
            print("Where are you going with to get that kind of money?")

        else:
            self.balance -= amount

# logout
    def logout(self) -> None:
        '''
        logout
        '''
        print(f"Goodbye {self.name}")
