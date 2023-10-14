# PasswordManager

Password manager for Cyber Security module

<h2>Cloning Repo</h2>
git init <br>
git clone https://github.com/KevinG2001/PasswordManager.git <br>
run pip install -r requirements.txt <br>
and you should be ready to go!

<h2>Creating Database</h2>
Run this script to create the database you
(Will be updated when adding new tables)<br>

CREATE DATABASE IF NOT EXISTS passwordmanager;

USE passwordmanager;

CREATE TABLE IF NOT EXISTS users (
    userID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

<h2>Database code for .env</h2>
DB_HOST=localhost<br>
DB_USER=root<br>
DB_NAME=passwordmanager<br>
DB_PASSWORD=your_password
