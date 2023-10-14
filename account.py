import mysql.connector
from dotenv import load_dotenv
import os

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
    password = input("Please enter your password")
    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
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
    # Executing the quary
    cursor.execute(searchUsername, (username,))

    # Getting the result of that username (getting the row)
    result = cursor.fetchone()
    # Checking to see if the password matches
    if result:
        if result[2] == password:
            print("Its a match")
        else:
            print("Not a match")
