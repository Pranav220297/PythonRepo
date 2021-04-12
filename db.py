import mysql.connector

def verifyUser(uid, passw):
    
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database = "mydb")

    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE userid ='" +uid+"'"
    cursor.execute(sql)
    info = cursor.fetchone()

    if(info!= None):
    
        if(passw == info[1]):
            return True
        else:
            return False
    else:
        return False
     
output = verifyUser('de','45')
print(output)

    
