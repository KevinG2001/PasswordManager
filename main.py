from account import login, createAccount
from passwords import createPassword, displayPasswords
import os


# Start of app
def main():
    one_or_two = int(input("1)Login\n2)Create Account"))
    if one_or_two == 1:
        userID, username = login()  # Called from account.py
        one_or_two = int(input("1)Create new password\n2)Display all passwords\n"))
        if one_or_two == 1:
            createPassword(userID)
        if one_or_two == 2:
            displayPasswords(userID)

    if one_or_two == 2:
        createAccount()  # Called from account.py
    else:
        print("Not an option please select 1 or 2")


if __name__ == "__main__":
    main()
