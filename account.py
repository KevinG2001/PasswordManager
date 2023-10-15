import mysql.connector
from dotenv import load_dotenv
import os
import hashlib, binascii

# loading the .env
load_dotenv()
# Getting information for the database from .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establishing connection to database
myDB = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    database=DB_NAME,
    password=DB_PASSWORD
)

uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetter = "abcdefghijklmnopqrstuvwxyz"
specialchar = "$@_#"
numericDigit = "0123456789"


def createAccount():
    cursor = myDB.cursor()  # Create a cursor
    # Boolean to see if the username is avaiable, will do this while loop until the username is avaiable
    usernameAvaiable = False
    while not usernameAvaiable:
        username = input(
            "Please enter your username")  # Takes input from the user and asigns it to a variable (Must add error check to makesure its not an INT)
        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        searchUsername = cursor.fetchone()
        if not searchUsername:
            usernameAvaiable = True
        else:
            print("Username in use")
            usernameAvaiable = False
    validPassword = False
    lowercaseValid = False
    uppercaseValid = False
    specialcharValid = False
    numericdigitValid = False
    while not validPassword:
        password = input(
            "Please enter a valid password\n Must contain a lower case and upper case letter,a numeric digit and a special character like $@_# "
            "and be 8 characters long")
        for i in password:
            if i in lowercaseLetter:
                lowercaseValid = True
            if i in uppercaseLetter:
                uppercaseValid = True
            if i in specialchar:
                specialcharValid = True
            if i in numericDigit:
                numericdigitValid = True
        if len(password) >= 8:
            passwordLengthValid = True
        if (
                lowercaseValid == True and uppercaseValid == True and specialcharValid == True and numericdigitValid == True and passwordLengthValid == True):
            validPassword = True
        else:
            validPassword = False

    # Turning password into string
    password = str(password)
    # Turning string into hash
    hashPass = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
    # Inserting hash into database
    values = (username, binascii.hexlify(hashPass))
    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(insert_query, values)
    myDB.commit()  # Commit the changes to the database
    # Close cursor and myDBconection when done
    cursor.close()
    myDB.close()


def login():
    cursor = myDB.cursor()
    username = input("Enter username")  # Getting the user to input there username
    password = input("Enter password")  # Getting the user to input there password
    # Searching the username in the database
    searchUsername = "SELECT * from users WHERE username = %s"
    # Executing the query
    cursor.execute(searchUsername, (username,))

    password = str(password)  # Turning password into string
    hashPass = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)  # Turning string into hash
    hexPass = binascii.hexlify(hashPass)  # Converting byte to hexadecimal
    hashPassStr = hexPass.decode('utf-8')  # decoding hexadecimal to string

    # Getting the result of that username (getting the row)
    result = cursor.fetchone()
    # Checking to see if the password matches
    if result:
        userID = result[0]
        username = result[1]
        if result[2] == hashPassStr:
            print("Log in successful")
            return userID, username
        else:
            print("Not a match")
    return None
