import base64

import mysql.connector
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from dotenv import load_dotenv
import os

# loading the .env
load_dotenv()
# Getting information for the database from .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
saltStr = os.getenv("saltStr")
# Turning salt to bytes
saltByte = saltStr.encode('utf-8')

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=saltByte,
    iterations=480000,
)

# taken from https://cryptography.io/en/latest/fernet/

# Key for password
f = Fernet(b'9w98hmJ4ROMc0jdDZvc0okdE7zEuctooCOP0aRlsmzA=')

# Establishing connection to database
myDB = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, database=DB_NAME, password=DB_PASSWORD
)


def createPassword(userID, email, password, platform):
    cursor = myDB.cursor()
    #Turning password into bytes
    passwordByte = password.encode('utf-8')
    print(userID, email, password, platform)

    # Encrypt password
    encryptedPass = f.encrypt(passwordByte)
    values = (platform, userID, email, encryptedPass)
    insert_query = "INSERT INTO passwords (platform, userID, email_username, password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, values)
    myDB.commit()
    cursor.close()
    myDB.close()


def displayPasswords(username):
    cursor = myDB.cursor()
    cursor.execute("SELECT * FROM passwords WHERE username = %s", (username,))
    searchByID = cursor.fetchall()
    print("Platform,     UserID,     ,Email,       Password")
    # print(key)

    for i in searchByID:
        platform, user_id, email, password = i
        passwordByte = password.encode('utf-8')
        decrypted_password = f.decrypt(passwordByte)
        print(f"{platform}, {user_id}, {email}, {decrypted_password}")

    cursor.close()
    myDB.close()
