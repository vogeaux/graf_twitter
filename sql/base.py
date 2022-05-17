import mysql.connector
import sys


  
  
myCon=mysql.connector.connect(host='localhost',
                        database='data',
                        user='root',
                        password='mypass')





mycursor = myCon.cursor()

def view():
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def insert_fake():
    sql = "INSERT INTO customers (time, id_tweet, text, username, name_politique) VALUES (%s, %s, %s, %s, %s)"
    val = ("2022-02-22 21:59:53","1496243211857281027", "arahTouati13 !","lubayle")
    mycursor.execute(sql, val)

    myCon.commit()

    print(mycursor.rowcount, "record inserted.")

def create():
    

    #mycursor.execute("CREATE TABLE customers (id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,time DATETIME, id_tweet VARCHAR(255), Text VARCHAR(800), Username VARCHAR(255))")
    mycursor.execute("CREATE TABLE customers (id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,nombre_jour BIGINT UNSIGNED NOT NULL,time DATETIME, id_tweet VARCHAR(800),likeCount BIGINT UNSIGNED NOT NULL, Text VARCHAR(800), Username VARCHAR(255), name_politique VARCHAR(800))")
    mycursor.execute("ALTER TABLE `customers` CONVERT TO CHARACTER SET utf8mb4;")
    mycursor.execute("GRANT ALL PRIVILEGES ON data.* TO python@localhost identified by 'python123';")


def create_database():
    mycursor.execute("CREATE DATABASE data DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;")

def drop_database():
    mycursor.execute("(DROP DATABASE [IF EXISTS] data;)")

def drop():
    sql = "DROP TABLE customers"

    mycursor.execute(sql)

try :
    if sys.argv[1] == 'create':
        create()
    if sys.argv[1] == 'view':
        view()
    if sys.argv[1] == 'drop':
        drop()
    if sys.argv[1] == 'insert_fake':
        insert_fake()

except :
    print ("erreur")