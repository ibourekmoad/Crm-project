import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Nadale@123654"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS crmtutorial")

print("Database created successfully")