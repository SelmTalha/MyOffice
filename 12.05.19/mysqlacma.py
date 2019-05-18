import mysql.connector


cnx = mysql.connector.connect(user='localhost', password='',
                              host='127.0.0.1',
                              database='employees')
                              
cnx.execute("CREATE DATABASES IF NOT EXISTS employees")
cnx.close()