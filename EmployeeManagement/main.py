from mainAdmin import adminMenuMgmt
from mainUser import userMenuMgmt
if (__name__ == '__main__'):
    print('''
        1. Admin Menu
        2. User Menu
    ''')

    ch = int(input("Enter the choice: "))
    if (ch == 1):
        un = "admin"
        pw = "admin123"
        username = input("Enter username: ")
        password = input("Enter password: ")
        if (un == username and pw == password):
            print("Login successful.")
            adminMenuMgmt()
        else:
            print("Invalid credentials.")
    elif (ch == 2):
        un = "user"
        pw = "user123"
        username = input("Enter username: ")
        password = input("Enter password: ")
        if (un == username and pw == password):
            print("Login successful.")
            userMenuMgmt()
        else:
            print("Invalid credentials.")

