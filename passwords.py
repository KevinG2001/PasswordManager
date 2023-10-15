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

uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetter = "abcdefghijklmnopqrstuvwxyz"
specialchar = "$@_#"
numericDigit = "0123456789"


def createPassword(userID):
    cursor = myDB.cursor()
    platform = input("Please enter the platform e.g. Youtube")
    email = input("Please enter your email")
    password = input("Please enter your password")
    values = (platform, userID, email, password)
    insert_query = "INSERT INTO passwords (platform, userid, email_username, password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, values)
    myDB.commit()
    cursor.close()
    myDB.close()