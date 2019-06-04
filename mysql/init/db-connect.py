import pymysql
from pymysql import Error
from time import sleep

a = False

while a == False: 
    try:
        mySQLconnection = pymysql.connect(host='mysql', database='mydb', user='myuser', password='mypass')
        mycursor = mySQLconnection.cursor()
        
        a = True 
        
        try:

            sql_query = """
            CREATE TABLE payment (
                payment_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                customer_id SMALLINT UNSIGNED NOT NULL,
                staff_id TINYINT UNSIGNED NOT NULL,
                rental_id INT DEFAULT NULL,
                amount DECIMAL(5,2) NOT NULL,
                payment_date DATETIME NOT NULL,
                last_update DATETIME NOT NULL,
                PRIMARY KEY  (payment_id))
            """

            mycursor.execute(sql_query)
            mySQLconnection.commit()

            print("Table payment created.")

        except Error as e:
            print("Table payment already exists.", e)

        try:

            sql_query = """
            CREATE TABLE paymentDate (
                paymentDate_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                amount DECIMAL(10,2) NOT NULL,
                payment_date DATETIME NOT NULL,
                PRIMARY KEY  (paymentDate_id))
            """

            mycursor.execute(sql_query)
            mySQLconnection.commit()

            print("Table paymentDate created.")

        except Error as e:
            print("Table paymentDate already exists.", e)   
        
        mycursor.close()
        mySQLconnection.close()

    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        sleep(1)
