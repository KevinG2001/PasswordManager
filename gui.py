import tkinter as tk
from account import login, createAccount


class GUI:
    def __init__(self):
        # Main Window
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry("750x500")
        self.mainWindow.title("Password Manager")
        self.mainWindow.resizable(False, False)

        self.makeLoginFrame()  # Calls the login frame

        # End of Gui
        self.mainWindow.mainloop()

    def getUsernameEntry(self):
        return self.usernameEntry.get()  # Gets the username from the entry field

    def getPasswordEntry(self):
        return self.passwordEntry.get()  # Gets the password from the entry field

    def login(self):
        username = self.getUsernameEntry()  # gets the username from the getmethods
        password = self.getPasswordEntry()  # gets the username from the getmethods
        result = login(username, password)  # Passes the username and password into the login function in account.py

    def makeLoginFrame(self):
        # Login Window
        self.loginFrame = tk.Frame(self.mainWindow)
        self.loginFrame.pack(pady=180)

        # Login Labels/entry
        self.usernameLbl = tk.Label(self.loginFrame, text="Username:")
        self.usernameLbl.grid(row=0, column=0, padx=(10, 0), pady=5, sticky='w')
        self.usernameEntry = tk.Entry(self.loginFrame)
        self.usernameEntry.grid(row=0, column=1, padx=(0, 10), pady=5)

        # Password Labels/entry
        self.passwordLbl = tk.Label(self.loginFrame, text="Password:")
        self.passwordLbl.grid(row=1, column=0, padx=(10, 0), pady=5, sticky='w')
        self.passwordEntry = tk.Entry(self.loginFrame)
        self.passwordEntry.grid(row=1, column=1, padx=(0, 10), pady=5)

        # Login Button
        loginBtn = tk.Button(self.loginFrame, text="Login", command=self.login)
        loginBtn.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        # Create account button
        createAccLbl = tk.Label(self.loginFrame, text="No account? Create Account!")
        createAccLbl.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        createAccLbl.bind("<Button-1>", lambda event: self.makeCreateAccFrame())

    def makeCreateAccFrame(self):
        print("Label clicked")
        if self.loginFrame:
            self.loginFrame.destroy()  # Destroy loginFrame if it exists

        self.CreateAccFrame = tk.Frame(self.mainWindow)
        self.CreateAccFrame.pack(pady=180)

        # Login Labels/entry
        self.usernameLbl = tk.Label(self.CreateAccFrame, text="Username:")
        self.usernameLbl.grid(row=0, column=0, padx=(10, 0), pady=5, sticky='w')
        self.usernameEntry = tk.Entry(self.CreateAccFrame)
        self.usernameEntry.grid(row=0, column=1, padx=(0, 10), pady=5)

        # Password Labels/entry
        self.passwordLbl = tk.Label(self.CreateAccFrame, text="Password:")
        self.passwordLbl.grid(row=1, column=0, padx=(10, 0), pady=5, sticky='w')
        self.passwordEntry = tk.Entry(self.CreateAccFrame)
        self.passwordEntry.grid(row=1, column=1, padx=(0, 10), pady=5)

        # Create Acc Button
        createAccBtn = tk.Button(self.CreateAccFrame, text="Create Account", command=self.createAcc)
        createAccBtn.grid(row=2, column=0, columnspan=2, pady=(0, 10))

    def createAcc(self):
        username = self.getUsernameEntry()  # gets the username from the getmethods
        password = self.getPasswordEntry()  # gets the username from the getmethods
        result = createAccount(username, password)  #  Passes the username and password into the createAccount function in account.py
        if result:
            result.mainloop()