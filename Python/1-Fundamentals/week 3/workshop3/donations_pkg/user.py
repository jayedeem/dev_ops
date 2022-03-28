def login(db: dict, username: str, password: str):

    if username in db.keys() and password in db.values():
        print("Logged in as admin")
    if username in db.keys() and password not in db.values():
        print("Incorrect password for admin")
    if username not in db.keys():
        print("User not found. Please register")
