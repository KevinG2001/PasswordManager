import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establish connection
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    database=DB_NAME,
    password=DB_PASSWORD
)

# Create a cursor
cursor = conn.cursor()


username = input("Please enter your username")
password = input("Please enter your password")

# Execute the INSERT statement
insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
values = (username, password)
cursor.execute(insert_query, values)

# Commit the changes
conn.commit()

# Close cursor and connection when done
cursor.close()
conn.close()