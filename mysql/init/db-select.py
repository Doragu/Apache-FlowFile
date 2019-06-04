import pymysql
from pymysql import Error
from time import sleep

a = False

while a == False: 
    try:
        mySQLconnection = pymysql.connect(host='localhost', database='mydb', user='myuser', password='mypass')
        mycursor = mySQLconnection.cursor()
        
        a = True 
                
        mycursor.execute("SELECT * FROM payment")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)        

        mycursor.close()
        mySQLconnection.close()
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        sleep(1)
        