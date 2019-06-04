import pymysql
from pymysql import Error
from time import sleep

a = False

while a == False: 
    try:
        mySQLconnection = pymysql.connect(host='localhost', database='mydb', user='myuser', password='mypass')
        mycursor = mySQLconnection.cursor()
        
        a = True 

        table = "payment"
                
        mycursor.execute("DROP table " + table)
        myresult = mycursor.fetchall()  

        mycursor.close()
        mySQLconnection.close()

        print("Table " + table + " dropped.")

    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        sleep(1)
        
