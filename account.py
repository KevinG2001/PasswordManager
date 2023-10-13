import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establish myDBection
myDB = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    database=DB_NAME,
    password=DB_PASSWORD
)


def createAccount():
    cursor = myDB.cursor()  # Create a cursor
    username = input("Please enter your username")
    password = input("Please enter your password")
    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(insert_query, values)
    myDB.commit()  # Commit the changes to the database
    # Close cursor and myDBection when done
    cursor.close()
    myDB.close()


def login():
    cursor = myDB.cursor()
    username = input("Enter username")
    password = input("Enter password")
    # Make sure to use placeholders in your query to prevent SQL injection
    searchUsername = "SELECT * from users WHERE username = %s"

    # Execute the query with the username as a parameter
    cursor.execute(searchUsername, (username,))

    # Fetch the result (assuming you want to fetch one row)
    result = cursor.fetchone()

    if result:
        if result[2] == password:
            print("Its a match")
        else:
            print("Not a match")



