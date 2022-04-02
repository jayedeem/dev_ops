"""User Related Logic"""


class HandleUser:
    """This handles backend"""

    def __init__(self, username: str, password: str, database) -> None:
        self.username = username
        self.password = password
        self.database = database

    def login(self) -> None:
        """Handle login"""
        # if not validate
        if self.username in self.database.keys() and self.password in self.database.values():
            print(f"Welcome {self.username}!")
        #take in username/password
        else:
            print("User not found, please try again or register")

        # validate
    def register(self) -> None:
        """Handle Registration"""
        # search user
        if self.username.lower() in self.database.keys():
            print("Username already exists")
        if len(self.username) > 10:
            print("Username must be less than 10 characters!")
        if len(self.password) <= 5:
            print("Password must be greater than 5 characters!")

        self.database[self.username] = self.password
