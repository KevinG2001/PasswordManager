import account

# Start of app
one_or_two = input("1)Login\n2)Create Account")
one_or_two = int(one_or_two)  # Convert the input to an integer
if one_or_two == 1:
    account.login()
if one_or_two == 2:
    account.createAccount()
else:
    print("Not an option please select 1 or 2")
