import mysql.connector


cursor = db.cursor()

def verifyUser():
    id =input("Pls enter id")
    passw =input("Pls enter password")

    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database = "mydb")

    info = cursor.execute("SELECT USERID , PASSWORD FROM USER WHERE USERID = id ")
    print(info)


verifyUser()
    


