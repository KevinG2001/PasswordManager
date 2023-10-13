import account

# Start of app
userinput = input("1)Login\n2)Create Account")
userinput = int(userinput)  # Convert the input to an integer
if userinput == 1:
    account.login()
else:
    account.createAccount()
