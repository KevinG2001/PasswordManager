import mysql.connector
from dotenv import load_dotenv
import os
import hashlib, binascii
import string

# loading the .env
load_dotenv()
# Getting information for the database from .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establishing connection to database
myDB = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, database=DB_NAME, password=DB_PASSWORD
)


def createAccount():
    cursor = myDB.cursor()

    # Get USERNAME
    while True:
        username = input("Please enter your username\n")

        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        searchUsername = cursor.fetchone()

        if searchUsername:
            print("Username in use")
        else:
            break

    # Get PASSWORD
    while True:
        password = input(
            "Please enter a valid password\n Must contain a lower case and upper case letter,a numeric digit and a special character like $@_# "
            "and be 8 characters long\n"
        )
        if is_valid_password(password):
            break

    # Turning string into hash
    hashPass = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), b"salt", 100000)

    # Inserting hash into database
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, binascii.hexlify(hashPass)),
    )

    myDB.commit()  # Commit the changes to the database

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
    hashPass = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), b"salt", 100000
    )  # Turning string into hash
    hexPass = binascii.hexlify(hashPass)  # Converting byte to hexadecimal
    hashPassStr = hexPass.decode("utf-8")  # decoding hexadecimal to string

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


def is_valid_password(password):
    return all(
        [
            any([x in string.ascii_lowercase for x in password]),
            any([x in string.ascii_uppercase for x in password]),
            any([x in string.punctuation for x in password]),
            any([x in string.digits for x in password]),
            len(password) >= 8,
        ]
    )
