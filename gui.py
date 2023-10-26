import tkinter as tk

from account import login, createAccount
from passwords import createPassword, getPasswords


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

    def getPlatformEntry(self):
        return self.PlatformEntry.get()  # Gets the playform from the entry field

    def login(self):
        username = self.getUsernameEntry()  # gets the username from the getmethods
        password = self.getPasswordEntry()  # gets the username from the getmethods
        result = login(username, password)  # Passes the username and password into the login function in account.py
        if result:
            userID = result[0]
            self.displayPasswordFrame(userID)
        else:
            alertWindow = tk.Toplevel()
            alertWindow.geometry("100x50")
            AlertLbl = tk.Label(alertWindow, text="Invalid Login")
            AlertLbl.pack()

    def makeLoginFrame(self):
        # Login Window
        self.loginFrame = tk.Frame(self.mainWindow)
        self.loginFrame.pack(pady=180)

        # Login Labels/entry
        self.usernameLbl = tk.Label(self.loginFrame, text="Username:")
        self.usernameLbl.grid(row=0, column=0, padx=(10, 0), pady=1, sticky='w')
        self.usernameEntry = tk.Entry(self.loginFrame)
        self.usernameEntry.grid(row=0, column=1, padx=(0, 10), pady=1)

        # Password Labels/entry
        self.passwordLbl = tk.Label(self.loginFrame, text="Password:")
        self.passwordLbl.grid(row=1, column=0, padx=(10, 0), pady=1, sticky='w')
        self.passwordEntry = tk.Entry(self.loginFrame)
        self.passwordEntry.grid(row=1, column=1, padx=(0, 10), pady=1)

        # Login Button
        loginBtn = tk.Button(self.loginFrame, text="Login", command=self.login)
        loginBtn.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        # Create account button
        createAccLbl = tk.Label(self.loginFrame, fg="blue", text="No account? Create Account!")
        createAccLbl.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        createAccLbl.bind("<Button-1>", lambda event: self.makeCreateAccFrame())

    def makeCreateAccFrame(self):
        if self.loginFrame:
            self.loginFrame.destroy()  # Destroy loginFrame if it exists

        self.CreateAccFrame = tk.Frame(self.mainWindow)
        self.CreateAccFrame.pack(pady=180)

        # Login Labels/entry
        self.usernameLbl = tk.Label(self.CreateAccFrame, text="Username:")
        self.usernameLbl.grid(row=0, column=0, padx=(10, 0), pady=1, sticky='w')
        self.usernameEntry = tk.Entry(self.CreateAccFrame)
        self.usernameEntry.grid(row=0, column=1, padx=(0, 10), pady=1)

        # Password Labels/entry
        self.passwordLbl = tk.Label(self.CreateAccFrame, text="Password:")
        self.passwordLbl.grid(row=1, column=0, padx=(10, 0), pady=1, sticky='w')
        self.passwordEntry = tk.Entry(self.CreateAccFrame)
        self.passwordEntry.grid(row=1, column=1, padx=(0, 10), pady=1)

        # Create Acc Button
        createAccBtn = tk.Button(self.CreateAccFrame, text="Create Account", command=self.createAcc)
        createAccBtn.grid(row=2, column=0, columnspan=2, pady=(0, 10))

    def createAcc(self):
        username = self.getUsernameEntry()  # gets the username from the getmethods
        password = self.getPasswordEntry()  # gets the username from the getmethods
        result = createAccount(username,
                               password)  # Passes the username and password into the createAccount function in account.py

        if result:
            result.mainloop()
        else:
            self.CreateAccFrame.destroy()
            self.makeLoginFrame()

    def displayPasswordFrame(self, userID):
        if self.loginFrame:
            self.loginFrame.destroy()

        self.passwordFrame = tk.Frame(self.mainWindow, height=425, bg="green")
        self.passwordFrame.pack(expand=1, fill=tk.BOTH)

        self.createPasswordFrame = tk.Frame(self.mainWindow, height=75, bg="black")
        self.createPasswordFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0)

        self.passwordHolder = tk.Frame(self.passwordFrame, bg="black", height=400, width=650)
        self.passwordHolder.pack(pady=15, expand=0)

        # CREATE ACCOUNT BUTTONS AND LABELS
        # Green part at bottom of GUI
        # Login Labels/entry
        self.PlatformLbl = tk.Label(self.createPasswordFrame, text="Platform:")
        self.PlatformLbl.grid(row=0, column=0, padx=(100, 10), pady=5)
        self.PlatformEntry = tk.Entry(self.createPasswordFrame)
        self.PlatformEntry.grid(row=0, column=1, columnspan=3, sticky="nsew", padx=(10, 10), pady=5)

        # Login Labels/entry
        self.usernameLbl = tk.Label(self.createPasswordFrame, text="Username/Email:")
        self.usernameLbl.grid(row=2, column=0, padx=(100, 10), pady=5)
        self.usernameEntry = tk.Entry(self.createPasswordFrame)
        self.usernameEntry.grid(row=2, column=1, padx=(10, 10), pady=5)

        # Password Labels/entry
        self.passwordLbl = tk.Label(self.createPasswordFrame, text="Password:")
        self.passwordLbl.grid(row=2, column=2, padx=(10, 10), pady=5)
        self.passwordEntry = tk.Entry(self.createPasswordFrame)
        self.passwordEntry.grid(row=2, column=3, padx=(10, 10), pady=5)

        createAccBtn = tk.Button(self.createPasswordFrame, text="Create Password",
                                 command=lambda: self.createPassword(userID))
        createAccBtn.grid(row=0, column=4, padx=(10, 100), pady=5)

        displayPassBtn = tk.Button(self.createPasswordFrame, text="Refresh Passwords",
                                   command=lambda: self.refreshPasswords(userID))
        displayPassBtn.grid(row=2, column=4, padx=(10, 100), pady=5)

    def createPassword(self, userID):
        email = self.getUsernameEntry()
        password = self.getPasswordEntry()
        platform = self.getPlatformEntry()

        createPassword(userID, email, password, platform)

    def refreshPasswords(self, userID):
        accRow = 0

        if self.passwordHolder.winfo_exists():
            for widget in self.passwordHolder.winfo_children():
                widget.destroy()

        for accDetails in getPasswords(userID):
            accRow += 1
            lblCol = 0
            # print(accDetails[0], accDetails[1], accDetails[2])
            self.AccountFrame = tk.Frame(self.passwordHolder, width=425)
            self.AccountFrame.grid(row=accRow)

            # Labels
            platformLbl = tk.Label(self.AccountFrame, text=f"Platform:", width=10)
            platformLbl.grid(row=0, column=0)
            # UserAccLabels
            UserPlatformLbl = tk.Label(self.AccountFrame, text=f"{accDetails[0]}", width=10)
            UserPlatformLbl.grid(row=0, column=lblCol + 1, padx=1)

            # Labels
            emailLbl = tk.Label(self.AccountFrame, text=f"Email:", width=10)
            emailLbl.grid(row=0, column=lblCol + 2, padx=(0, 0))
            # UserAccLabels
            UserEmailLbl = tk.Label(self.AccountFrame, text=f"{accDetails[1]}")
            UserEmailLbl.grid(row=0, column=lblCol + 3)

            # Labels
            passwordLbl = tk.Label(self.AccountFrame, text=f"Password:", width=10)
            passwordLbl.grid(row=0, column=lblCol + 4, padx=(0, 0))
            # UserAccLabels
            UserPasswordLbl = tk.Label(self.AccountFrame, text=f"{accDetails[2]}", width=10)
            UserPasswordLbl.grid(row=0, column=lblCol + 5)
