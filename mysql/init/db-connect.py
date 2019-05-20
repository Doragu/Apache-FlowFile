import mysql.connector
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host='localhost', database='mydb', user='myuser', password='mypass')
    
    sql_query = """CREATE TABLE payment (
        payment_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
        customer_id SMALLINT UNSIGNED NOT NULL,
        staff_id TINYINT UNSIGNED NOT NULL,
        rental_id INT DEFAULT NULL,
        amount DECIMAL(5,2) NOT NULL,
        payment_date DATETIME NOT NULL,
        last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY  (payment_id)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    mycursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)

finally:
    if (mySQLconnection.is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")
