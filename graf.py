# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
 
 
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="mypass",
                               database="data")
mycursor = mydb.cursor()
 
# Fecthing Data From mysql to my python progame
mycursor.execute("SELECT time,likeCount FROM customers")
result = mycursor.fetchall
 
time = []
likeCount = []
 
for i in mycursor:
    time.append(i[0])
    likeCount.append(i[1])
     
print("time = ", time)
print("Marks of likeCount = ", likeCount)
 
 
# Visulizing Data using Matplotlib
plt.bar(time,likeCount)
plt.ylim(0, 400)
plt.xlabel("time")
plt.ylabel("Marks of likeCount")
plt.title("1er_test")
plt.show()