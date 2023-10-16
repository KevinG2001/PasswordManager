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
    host=DB_HOST, user=DB_USER, database=DB_NAME, password=DB_PASSWORD
)


def createPassword(userID):
    cursor = myDB.cursor()
    platform = input("Please enter the platform e.g. Youtube")
    email = input("Please enter your email\n")
    password = input("Please enter your password\n")
    values = (platform, userID, email, password)
    insert_query = "INSERT INTO passwords (platform, userid, email_username, password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, values)
    myDB.commit()
    cursor.close()
    myDB.close()


def displayPasswords(userID):
    cursor = myDB.cursor()
    cursor.execute("SELECT * FROM passwords WHERE userID = %s", (userID,))
    searchByID = cursor.fetchall()
    print("Platform,     UserID,     ,Email,       Password")
    for i in searchByID:
        print(i)

    cursor.close()
    myDB.close()
